from database import connect_database
import matplotlib.pyplot as plt
def histogram_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT price FROM products""")
    data=cursor.fetchall()
    price=[]
    for row in data:
        price.append(float(row[0]))
    fig=plt.figure(figsize=(10,6))
    fig.set_facecolor("#e54242")
    ax=plt.gca()
    ax.set_facecolor("#05f93a")
    plt.hist(price,bins=5,color="orange",edgecolor="black",linewidth=2,alpha=0.8,label="Product price")
    plt.title("Product Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    cursor.close()
    conn.close()
    
