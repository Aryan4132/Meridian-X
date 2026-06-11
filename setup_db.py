import sqlite3
import os

def generate_sample_db():
    db_path = "sample_shop.db"
    if os.path.exists(db_path):
        os.remove(db_path)
        
    print(f"[Setup DB] Generating '{db_path}'...")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)
    
    cursor.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER NOT NULL
    );
    """)
    
    cursor.execute("""
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        total REAL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(product_id) REFERENCES products(id)
    );
    """)
    
    # Insert mock users
    users = [
        ("Aryan", "aryan@example.com"),
        ("John Doe", "john@example.com"),
        ("Alice Smith", "alice@example.com"),
        ("Bob Miller", "bob@example.com"),
        ("Emma Watson", "emma@example.com")
    ]
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?);", users)
    
    # Insert mock products
    products = [
        ("Wireless Mouse", 25.99, 120),
        ("Mechanical Keyboard", 89.99, 45),
        ("27-inch Monitor", 199.99, 30),
        ("USB-C Hub", 19.99, 85),
        ("Noise Cancelling Headphones", 149.99, 15)
    ]
    cursor.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?);", products)
    
    # Insert mock orders
    orders = [
        (1, 1, 2, 51.98), # Aryan ordered 2 mice
        (2, 2, 1, 89.99), # John ordered 1 keyboard
        (1, 3, 1, 199.99), # Aryan ordered 1 monitor
        (3, 4, 3, 59.97), # Alice ordered 3 USB hubs
        (4, 5, 1, 149.99) # Bob ordered 1 headphones
    ]
    cursor.executemany("INSERT INTO orders (user_id, product_id, quantity, total) VALUES (?, ?, ?, ?);", orders)
    
    conn.commit()
    conn.close()
    print(f"[Setup DB] Successfully generated '{db_path}' with sample schemas and entries.")

if __name__ == "__main__":
    generate_sample_db()
