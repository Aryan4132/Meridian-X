import os
import sqlite3
import ollama
import threading
from typing import List, Dict, Any, Optional
from database import get_ollama_client_host

# Active connection state variables
_conn = None
_conn_type = ""
_conn_dsn = ""
_db_lock = threading.RLock()

def _get_active_model() -> str:
    return os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")

def db_connect(type: str, path_or_dsn: str) -> str:
    """Connect to a local database ('sqlite', 'postgresql', or 'mysql')."""
    global _conn, _conn_type, _conn_dsn
    db_type = type.lower()
    
    with _db_lock:
        if _conn:
            db_disconnect()
            
        try:
            if db_type == "sqlite":
                # Connect to SQLite file
                _conn = sqlite3.connect(path_or_dsn)
                _conn_type = "sqlite"
                _conn_dsn = path_or_dsn
                return f"Successfully connected to local SQLite database at '{path_or_dsn}'."
                
            elif db_type == "postgresql":
                import psycopg2
                _conn = psycopg2.connect(path_or_dsn)
                _conn_type = "postgresql"
                _conn_dsn = path_or_dsn
                return f"Successfully connected to local PostgreSQL database."
                
            elif db_type == "mysql":
                import pymysql
                # Parse simple dsn or host parameters
                # Assumes format: username:password@host:port/dbname
                _conn = pymysql.connect(dsn=path_or_dsn)
                _conn_type = "mysql"
                _conn_dsn = path_or_dsn
                return f"Successfully connected to local MySQL database."
                
            else:
                return f"Error: Unsupported database type '{type}'. Supported: sqlite, postgresql, mysql."
        except Exception as e:
            return f"Failed to connect to database: {e}"

def db_disconnect() -> str:
    """Close the active database connection."""
    global _conn, _conn_type, _conn_dsn
    with _db_lock:
        if not _conn:
            return "No active database connection to close."
        try:
            _conn.close()
            msg = f"Closed active {_conn_type} connection to '{_conn_dsn}'."
            _conn = None
            _conn_type = ""
            _conn_dsn = ""
            return msg
        except Exception as e:
            return f"Error closing connection: {e}"

def db_query(sql: str) -> str:
    """Execute a SQL SELECT statement and return rows as a formatted string."""
    global _conn
    with _db_lock:
        if not _conn:
            return "Error: No active database connection. Call db_connect first."
            
        try:
            cursor = _conn.cursor()
            cursor.execute(sql)
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            
            if not rows:
                return "Query completed. 0 rows returned."
                
            # Format as markdown table
            lines = []
            # Header
            lines.append("| " + " | ".join(columns) + " |")
            lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
            # Rows
            for row in rows[:50]: # Limit to top 50 rows
                row_strs = [str(x).replace("\n", " ") for x in row]
                lines.append("| " + " | ".join(row_strs) + " |")
                
            summary = "\n".join(lines)
            if len(rows) > 50:
                summary += f"\n\n(Truncated: returned {len(rows)} rows, showing first 50)"
            return summary
        except Exception as e:
            return f"SQL Query execution failed: {e}"

def db_execute(sql: str) -> str:
    """Execute an INSERT, UPDATE, or DELETE SQL statement."""
    global _conn
    with _db_lock:
        if not _conn:
            return "Error: No active database connection. Call db_connect first."
            
        try:
            cursor = _conn.cursor()
            cursor.execute(sql)
            _conn.commit()
            return f"SQL statement executed successfully. Affected rows: {cursor.rowcount}"
        except Exception as e:
            return f"SQL Execution failed: {e}"

def db_schema() -> str:
    """List all tables, columns, types, and primary keys of the connected database."""
    global _conn, _conn_type
    with _db_lock:
        if not _conn:
            return "Error: No active database connection. Call db_connect first."
            
        try:
            cursor = _conn.cursor()
            tables_info = []
            
            if _conn_type == "sqlite":
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = [row[0] for row in cursor.fetchall() if not row[0].startswith("sqlite_")]
                
                for t in tables:
                    cursor.execute(f"PRAGMA table_info({t});")
                    cols = cursor.fetchall()
                    col_defs = []
                    for c in cols:
                        # c is (cid, name, type, notnull, dflt_value, pk)
                        pk_str = " (PK)" if c[5] else ""
                        col_defs.append(f"{c[1]} {c[2]}{pk_str}")
                    tables_info.append(f"Table '{t}':\n  " + ", ".join(col_defs))
                    
            elif _conn_type == "postgresql" or _conn_type == "mysql":
                cursor.execute(
                    "SELECT table_name FROM information_schema.tables WHERE table_schema='public';"
                    if _conn_type == "postgresql" else
                    "SHOW TABLES;"
                )
                tables = [row[0] for row in cursor.fetchall()]
                for t in tables:
                    cursor.execute(f"DESCRIBE {t};" if _conn_type == "mysql" else f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name='{t}';")
                    cols = cursor.fetchall()
                    col_defs = [f"{c[0]} {c[1]}" for c in cols]
                    tables_info.append(f"Table '{t}':\n  " + ", ".join(col_defs))
                    
            if not tables_info:
                return "Connected database has no tables."
            return "Database Schema Information:\n\n" + "\n".join(tables_info)
        except Exception as e:
            return f"Failed to retrieve database schema: {e}"

def db_nl_query(natural_language: str) -> str:
    """Translate natural language text to SQL using the current schema, and run it."""
    global _conn
    with _db_lock:
        if not _conn:
            return "Error: No active database connection. Call db_connect first."
            
        schema = db_schema()
        if schema.startswith("Error"):
            return "Error: Could not retrieve schema to generate SQL query."
            
        try:
            client = ollama.Client(host=get_ollama_client_host())
            prompt = (
                f"You are a database query generator. Translate the following plain-English request "
                f"into a single valid SQL SELECT query based on the active schema:\n\n"
                f"Active Database Type: {_conn_type}\n\n"
                f"Active Schema:\n{schema}\n\n"
                f"User Request: {natural_language}\n\n"
                f"Respond with ONLY the raw SQL query. Do not wrap in markdown fences or explanations."
            )
            res = client.generate(model=_get_active_model(), prompt=prompt)
            sql = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
            
            # Clean formatting
            if sql.startswith("```"):
                sql = sql.strip("`").replace("sql\n", "").strip()
                
            print(f"[DB Query] Translated: '{natural_language}' -> SQL: '{sql}'")
            query_res = db_query(sql)
            return f"Generated SQL: {sql}\n\nQuery Results:\n{query_res}"
        except Exception as e:
            return f"Error executing Natural Language SQL query: {e}"
