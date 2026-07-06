import os
import socket
import threading
import json
import time
from typing import List, Dict, Any
from database import get_mongo_db, db

P2P_PORT = 8009
UDP_DISCOVERY_PORT = 8010
_server_running = False

class P2PSyncNode:
    def __init__(self, host="0.0.0.0", port=P2P_PORT):
        self.host = host
        self.port = port
        self.peers = set()
        self.lock = threading.Lock()
        self.tcp_socket = None
        self.udp_socket = None

    def start(self):
        global _server_running
        if _server_running:
            return "P2P Sync server is already active."
        _server_running = True
        
        # Start TCP listener for database sync
        threading.Thread(target=self._run_tcp_server, daemon=True).start()
        # Start UDP listener for peer discovery
        threading.Thread(target=self._run_udp_discovery_listener, daemon=True).start()
        # Start UDP broadcast thread
        threading.Thread(target=self._run_udp_broadcast, daemon=True).start()
        
        return f"P2P Sync daemon started on {self.host}:{self.port}."

    def stop(self) -> str:
        global _server_running
        if not _server_running:
            return "P2P Sync server is not active."
        _server_running = False
        
        # Close sockets to unblock accept() and recvfrom()
        if self.tcp_socket:
            try:
                self.tcp_socket.close()
            except Exception:
                pass
        if self.udp_socket:
            try:
                self.udp_socket.close()
            except Exception:
                pass
                
        return "P2P Sync daemon stopped."

    def _run_tcp_server(self):
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.tcp_socket.bind((self.host, self.port))
            self.tcp_socket.listen(5)
            print(f"[P2P Sync] TCP Server listening on port {self.port}...")
            while _server_running:
                conn, addr = self.tcp_socket.accept()
                threading.Thread(target=self._handle_client, args=(conn, addr), daemon=True).start()
        except Exception as e:
            if _server_running:
                print(f"[P2P Sync] TCP Server error: {e}")
        finally:
            self.tcp_socket.close()

    def _handle_client(self, conn, addr):
        try:
            chunks = []
            while True:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                chunks.append(chunk)
            data = b"".join(chunks).decode('utf-8')
            
            if not data.strip():
                return
                
            payload = json.loads(data)
            action = payload.get("action")
            
            if action == "sync_request":
                # Check cryptographic validation token
                local_token = os.environ.get("P2P_SECRET_TOKEN", "")
                peer_token = payload.get("token", "")
                if local_token and peer_token != local_token:
                    print(f"[P2P Sync] REJECTED unauthorized sync request from {addr[0]} (invalid token)")
                    conn.sendall(json.dumps({"status": "error", "message": "Unauthorized: Invalid P2P_SECRET_TOKEN"}).encode('utf-8'))
                    return

                # Received peer's database state. Perform similarity merge.
                print(f"[P2P Sync] Sync request received from {addr[0]}")
                response = self._merge_peer_state(payload.get("data", {}))
                conn.sendall(json.dumps({"status": "success", "data": response}).encode('utf-8'))
        except Exception as e:
            print(f"[P2P Sync] Error handling client {addr}: {e}")
        finally:
            conn.close()

    def _run_udp_discovery_listener(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.udp_socket.bind(("0.0.0.0", UDP_DISCOVERY_PORT))
            print(f"[P2P Sync] UDP Discovery listening on port {UDP_DISCOVERY_PORT}...")
            while _server_running:
                data, addr = self.udp_socket.recvfrom(1024)
                msg = data.decode('utf-8').strip()
                if msg.startswith("MERIDIAN_PEER:"):
                    remainder = msg[len("MERIDIAN_PEER:"):]
                    parts = remainder.rsplit(":", 1)
                    peer_port = int(parts[-1])
                    peer_ip = addr[0]
                    # Don't add ourselves
                    try:
                        local_ips = {info[4][0] for info in socket.getaddrinfo(socket.gethostname(), None)}
                        local_ips.update({"127.0.0.1", "::1", "0.0.0.0"})
                    except Exception:
                        local_ips = {"127.0.0.1", "::1"}
                    if peer_ip not in local_ips or peer_port != self.port:
                        with self.lock:
                            if (peer_ip, peer_port) not in self.peers:
                                self.peers.add((peer_ip, peer_port))
                                print(f"[P2P Sync] Discovered new peer: {peer_ip}:{peer_port}")
        except Exception as e:
            if _server_running:
                print(f"[P2P Sync] UDP Discovery listener error: {e}")
        finally:
            self.udp_socket.close()

    def _run_udp_broadcast(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        print("[P2P Sync] UDP Broadcaster initialized.")
        while _server_running:
            try:
                msg = f"MERIDIAN_PEER:{self.port}"
                s.sendto(msg.encode('utf-8'), ('255.255.255.255', UDP_DISCOVERY_PORT))
            except Exception:
                pass
            time.sleep(10)  # Broadcast every 10 seconds
        s.close()

    def _merge_peer_state(self, peer_data: Dict[str, Any]) -> Dict[str, Any]:
        """Merges incoming peer items into local Turbovec caches and MongoDB KG."""
        merged_facts = 0
        merged_caches = 0
        
        # 1. Merge Knowledge Graph Facts
        db_conn = get_mongo_db()
        if db_conn is not None:
            try:
                collection = db_conn["knowledge_graph"]
                peer_facts = peer_data.get("knowledge_graph", [])
                for fact in peer_facts:
                    entity = fact.get("entity")
                    relation = fact.get("relation")
                    target = fact.get("target")
                    if entity and relation and target:
                        # Avoid duplicates: update timestamp
                        collection.update_one(
                            {"entity": entity, "relation": relation, "target": target},
                            {"$set": {"timestamp": time.time()}},
                            upsert=True
                        )
                        merged_facts += 1
            except Exception as e:
                print(f"[P2P Sync] Knowledge graph merge failed: {e}")

        # 2. Merge Turbovec Semantic Caches
        try:
            from database import add_to_semantic_cache, check_semantic_cache, get_sqlite_conn
            peer_caches = peer_data.get("semantic_cache", [])
            existing_queries = set()
            try:
                conn = get_sqlite_conn()
                cursor = conn.cursor()
                cursor.execute("SELECT query_text FROM semantic_cache")
                existing_queries = {r["query_text"] for r in cursor.fetchall()}
                conn.close()
            except Exception as dbe:
                print(f"[P2P Sync] Failed to pre-fetch cache queries: {dbe}")

            for cache in peer_caches:
                query_text = cache.get("query_text")
                response_text = cache.get("response_text")
                if query_text and response_text:
                    if query_text in existing_queries:
                        continue
                    # Check if already exists in cache (semantic similarity check fallback)
                    existing = check_semantic_cache(query_text)
                    if not existing:
                        ttl = int(cache.get("expires_at", time.time() + 86400) - time.time())
                        if ttl > 0:
                            add_to_semantic_cache(query_text, response_text, ttl_seconds=ttl)
                            merged_caches += 1
        except Exception as e:
            print(f"[P2P Sync] Turbovec merge failed: {e}")

        print(f"[P2P Sync] Merge complete: +{merged_facts} facts, +{merged_caches} caches.")
        return {"merged_facts": merged_facts, "merged_caches": merged_caches}

    def sync_now(self) -> str:
        """Manually trigger outbound sync to all discovered peers."""
        if not self.peers:
            return "No local network peers discovered yet."

        # Fetch local data to send
        local_data = {"knowledge_graph": [], "semantic_cache": []}
        
        # Load local facts
        db_conn = get_mongo_db()
        if db_conn is not None:
            try:
                collection = db_conn["knowledge_graph"]
                local_data["knowledge_graph"] = list(collection.find({}, {"_id": 0}))
            except Exception:
                pass
                
        # Load local semantic cache
        try:
            from database import get_sqlite_conn
            conn = get_sqlite_conn()
            cursor = conn.cursor()
            cursor.execute("SELECT query_text, response_text, expires_at FROM semantic_cache LIMIT 200")
            rows = cursor.fetchall()
            conn.close()
            local_data["semantic_cache"] = [
                {
                    "query_text": r["query_text"],
                    "response_text": r["response_text"],
                    "expires_at": r["expires_at"]
                }
                for r in rows
            ]
        except Exception:
            pass

        sync_summary = []
        for peer_ip, peer_port in list(self.peers):
            s = None
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3.0)
                s.connect((peer_ip, peer_port))
                
                payload = {
                    "action": "sync_request",
                    "token": os.environ.get("P2P_SECRET_TOKEN", ""),
                    "data": local_data
                }
                s.sendall(json.dumps(payload).encode('utf-8'))
                s.shutdown(socket.SHUT_WR)
                
                # Receive confirmation
                chunks = []
                while True:
                    chunk = s.recv(4096)
                    if not chunk:
                        break
                    chunks.append(chunk)
                resp = b"".join(chunks).decode('utf-8')
                result = json.loads(resp)
                if result.get("status") == "success":
                    m_data = result.get("data", {})
                    sync_summary.append(f"Synced with {peer_ip}:{peer_port} (merged {m_data.get('merged_facts')} facts, {m_data.get('merged_caches')} caches)")
                else:
                    sync_summary.append(f"Rejected by {peer_ip}:{peer_port}: {result.get('message')}")
            except Exception as e:
                sync_summary.append(f"Failed to sync with {peer_ip}:{peer_port}: {e}")
            finally:
                if s:
                    try:
                        s.close()
                    except Exception:
                        pass
                
        return "\n".join(sync_summary)

# Global Node instance
p2p_node = P2PSyncNode()
