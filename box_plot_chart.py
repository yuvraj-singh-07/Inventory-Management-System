from database import connect_database
import matplotlib.pyplot as plt
def box_plot_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT price FROM products""")
    data=cursor.fetchall()
    price=[]
    for row in data:
        price.append(float(row[0]))
    fig=plt.figure(figsize=(10,6))
    fig.set_facecolor("#e96969")
    ax=plt.gca()
    ax.set_facecolor("#83d483")
    plt.boxplot(price, vert=True, showmeans=True, meanline=True, notch=True,
                tick_labels=["Products"])
    plt.title("Inventory Product Price Analysis")
    plt.xlabel("Product")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    cursor.close()
    conn.close()
