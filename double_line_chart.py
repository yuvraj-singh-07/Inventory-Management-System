from database import connect_database
import matplotlib.pyplot as plt
def double_line_chart():
    conn,cursor = connect_database()
    cursor.execute("""SELECT product_name, price, quantity FROM products""")
    data=cursor.fetchall()
    product_name=[]
    price=[]
    quantity=[]
    for row in data:
        product_name.append(row[0])
        price.append(row[1])
        quantity.append(row[2])
    plt.figure(figsize=(10,5))
    plt.plot(product_name,price,marker="s",linewidth=2,linestyle="--",label="Price",color="Red")
    plt.plot(product_name,quantity,marker="o",linewidth=2,linestyle="-",label="Quantity",color="Green")
    plt.title("Inventory Product by Quantity")
    plt.xlabel("Product Name")
    plt.ylabel("Quantity")
    plt.grid(True)
    plt.legend()
    plt.show()
    cursor.close()
    conn.close()
