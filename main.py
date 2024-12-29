import tkinter as tk
from tkinter import messagebox

# الشاشة الرئيسية
root = tk.Tk()
root.title("مكتبة الهدي - برنامج مبيعات")
root.geometry("800x600")
root.configure(bg='#f0f0f0')

# عنوان رئيسي
title = tk.Label(root, text="📚 مكتبة الهدي - برنامج المبيعات", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
title.pack(pady=20)

# الأزرار الرئيسية
def open_sales():
    messagebox.showinfo("المبيعات", "هنا شاشة المبيعات")

def open_purchases():
    messagebox.showinfo("المشتريات", "هنا شاشة المشتريات")

def add_product():
    messagebox.showinfo("إضافة منتج", "هنا شاشة إضافة منتج")

sales_btn = tk.Button(root, text="💵 المبيعات", font=("Arial", 14), command=open_sales)
sales_btn.pack(pady=10)

purchases_btn = tk.Button(root, text="📦 المشتريات", font=("Arial", 14), command=open_purchases)
purchases_btn.pack(pady=10)

add_product_btn = tk.Button(root, text="➕ إضافة منتج", font=("Arial", 14), command=add_product)
add_product_btn.pack(pady=10)

# إنهاء البرنامج
exit_btn = tk.Button(root, text="❌ خروج", font=("Arial", 14), command=root.quit)
exit_btn.pack(pady=30)

root.mainloop()
