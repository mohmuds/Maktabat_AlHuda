import sqlite3
import matplotlib.pyplot as plt

def show_sales_report():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    cursor.execute("SELECT date, SUM(total) FROM sales GROUP BY date")
    data = cursor.fetchall()
    conn.close()
    
    dates = [row[0] for row in data]
    totals = [row[1] for row in data]
    
    plt.figure(figsize=(10, 5))
    plt.bar(dates, totals, color='skyblue')
    plt.xlabel('التاريخ')
    plt.ylabel('إجمالي المبيعات')
    plt.title('تقرير المبيعات')
    plt.show()

show_sales_report()
