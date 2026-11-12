from database import connect_database
import matplotlib.pyplot as plt
def bar_chart():
    conn,cursor = connect_database()
    cursor.execute("""SELECT product_name, quantity FROM products""")
    data=cursor.fetchall()
    product_name=[]
    quantity=[]
    for row in data:
        product_name.append(row[0])
        quantity.append(row[1])
    plt.figure(figsize=(10,5))
    plt.bar(product_name,quantity,width=0.5,label="Stock Quantity")
    plt.title("Inventory Product by Quantity")
    plt.xlabel("Product Name")
    plt.ylabel("Quantity")
    plt.grid(True)
    plt.legend()
    plt.show()
    cursor.close()
    conn.close()
