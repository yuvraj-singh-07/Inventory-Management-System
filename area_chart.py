from database import connect_database
import matplotlib.pyplot as plt
def area_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT product_name , quantity FROM products""")
    data=cursor.fetchall()
    product_name = []
    quantity = []
    for row in data:
        product_name.append(row[0])
        quantity.append(row[1])
    fig=plt.figure(figsize=(10,6))
    fig.set_facecolor("#ae8f32")
    ax=plt.gca()
    ax.set_facecolor("#00f00f")
    plt.plot(product_name,quantity,color="blue",marker="o",markersize=8,label="Stock Quantity")
    plt.fill_between(product_name,quantity,color="skyblue",alpha=0.5)
    plt.title("Inventory Stock Area Chart")
    plt.xlabel("Product Name",fontsize=12)
    plt.ylabel("Quantity",fontsize=12)
    plt.xticks(rotation=20)
    plt.legend()
    plt.grid(True,linestyle="--",alpha=0.5)
    plt.tight_layout() #automatic layout set
    plt.show()
    cursor.close()
    conn.close()
