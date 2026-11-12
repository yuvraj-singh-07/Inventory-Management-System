from database import connect_database
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
def seaborn_line_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT product_name,quantity FROM products""")
    data=cursor.fetchall()
    df = pd.DataFrame(data,columns=["Product","Quantity"])
    sb.set_theme(style="darkgrid",palette="deep",font_scale=1.1)
    fig=plt.figure(figsize=(10,6))
    fig.set_facecolor("lightblue")
    ax=plt.gca()
    ax.set_facecolor("#ebdea2")
    sb.lineplot(data=df,x="Product",y="Quantity",markers="o",markersize=10,linewidth=3,linestyle="--",label="Stock")
    plt.title("Inventory Stock Analysis")
    plt.xlabel("Product Name")
    plt.ylabel("Quantity")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    cursor.close()
    conn.close()
