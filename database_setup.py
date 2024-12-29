import sqlite3

# إنشاء قاعدة البيانات
conn = sqlite3.connect('store.db')
cursor = conn.cursor()

# إنشاء جدول المنتجات
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL,
    category TEXT
)
''')

# إنشاء جدول المبيعات
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    total REAL,
    date TEXT,
    FOREIGN KEY (product_id) REFERENCES products (id)
)
''')

# إنشاء جدول المشتريات
cursor.execute('''
CREATE TABLE IF NOT EXISTS purchases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    quantity INTEGER,
    total REAL,
    date TEXT,
    FOREIGN KEY (product_id) REFERENCES products (id)
)
''')

conn.commit()
conn.close()
print("✅ تم إنشاء قاعدة البيانات بنجاح!")
