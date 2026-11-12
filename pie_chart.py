from database import connect_database
import matplotlib.pyplot as plt
def pie_chart():
    conn,cursor = connect_database()
    cursor.execute("""SELECT product_name, quantity FROM products""")
    data=cursor.fetchall()
    product_name=[]
    quantity=[]
    for row in data:
        product_name.append(row[0])
        quantity.append(row[1])
    if not data:
        print("No products available to chart.")
        cursor.close()
        conn.close()
        return
    plt.figure(figsize=(8,8))
    colors=plt.cm.tab20.colors[:len(product_name)]
    plt.pie(quantity,labels=product_name,colors=colors,autopct="%1.1f%%",startangle=90,explode=[0.05]*len(product_name),shadow=True,radius=1.2,counterclock=True,wedgeprops={"edgecolor" : "black","linewidth" : 1})
    plt.title("Product Quantity Distribution")
    plt.axis("equal")
    plt.legend()
    plt.show()
    cursor.close()
    conn.close()
