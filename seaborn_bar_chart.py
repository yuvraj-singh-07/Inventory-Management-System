from database import connect_database
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
def seaborn_bar_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT product_name,quantity FROM products""")
    data=cursor.fetchall()
    df = pd.DataFrame(data, columns=["Product", "Quantity"])
    sb.set_theme(style="whitegrid",palette="Set2",font_scale=1.2)
    fig=plt.figure(figsize=(11,6))
    fig.set_facecolor("#ff35a7")
    ax=plt.gca()
    ax.set_facecolor("#e96969")
    sb.barplot(data=df,x="Product",y="Quantity",linewidth=2,width=0.6,edgecolor="black",saturation=0.9,label="Stock")
    plt.title("Inventory Stock Bar Chart",fontsize=16,fontweight="bold")
    plt.xlabel("Product Name",fontsize=12)
    plt.ylabel("Quantity",fontsize=12)
    plt.xticks(rotation=20)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    cursor.close()
    conn.close()