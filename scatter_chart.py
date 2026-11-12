from database import connect_database
import matplotlib.pyplot as plt
def scatter_chart():
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
    fig=plt.figure(figsize=(10,6))
    fig.set_facecolor("lightgrey")
    ax=plt.gca()
    ax.set_facecolor("Lightyellow")
    plt.scatter(price,quantity,s=250,marker="o",c="orange",alpha=0.5,edgecolors="black",linewidths=2,label="Products")
    for i in range(len(product_name)):
        plt.text(price[i],quantity[i],product_name[i],fontsize=9)
    plt.title("Price vs Quantity")
    plt.xlabel("Price")
    plt.ylabel("Quantity")
    plt.grid(True)
    plt.legend()
    plt.show()
    cursor.close()
    conn.close()
