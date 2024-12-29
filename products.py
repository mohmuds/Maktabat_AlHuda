import sqlite3
from tkinter import *

def add_product():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    name = product_name.get()
    price = float(product_price.get())
    quantity = int(product_quantity.get())
    category = product_category.get()
    
    cursor.execute("INSERT INTO products (name, price, quantity, category) VALUES (?, ?, ?, ?)", 
                   (name, price, quantity, category))
    conn.commit()
    conn.close()
    print("✅ تم إضافة المنتج بنجاح!")

# واجهة إضافة منتج
root = Tk()
root.title("إضافة منتج جديد")
root.geometry("400x400")

Label(root, text="اسم المنتج").pack()
product_name = Entry(root)
product_name.pack()

Label(root, text="السعر").pack()
product_price = Entry(root)
product_price.pack()

Label(root, text="الكمية").pack()
product_quantity = Entry(root)
product_quantity.pack()

Label(root, text="الفئة").pack()
product_category = Entry(root)
product_category.pack()

Button(root, text="إضافة المنتج", command=add_product).pack(pady=20)
root.mainloop()
