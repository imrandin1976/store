import sqlite3

def init_db():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        barcode TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def get_product(barcode):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, quantity FROM products WHERE barcode = ?", (barcode,))
    result = cursor.fetchone()
    conn.close()
    return result

def update_stock(barcode, qty_change):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET quantity = quantity + ? WHERE barcode = ?", (qty_change, barcode))
    conn.commit()
    conn.close()

def add_or_update_product(barcode, name, price, quantity):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO products (barcode, name, price, quantity)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(barcode) DO UPDATE SET
        name = excluded.name,
        price = excluded.price,
        quantity = quantity + excluded.quantity
    ''', (barcode, name, price, quantity))
    conn.commit()
    conn.close()
