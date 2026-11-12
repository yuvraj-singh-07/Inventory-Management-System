from database import connect_database
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
def seaborn_histogram_plot_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT price FROM products""")
    data=cursor.fetchall()
    df=pd.DataFrame(data,columns=["Price"])
    sb.set_theme(style="whitegrid",palette="Set2",font_scale=1.2)
    fig=plt.figure(figsize=(10,6))
    fig.set_facecolor("#e54242")
    ax=plt.gca()
    ax.set_facecolor("#05f93a")
    sb.histplot(data=df,x="Price",bins=8,color="orange",edgecolor="black",linewidth=2,alpha=0.8,label="product price") #vertical to horizontal
    plt.title("Product Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    cursor.close()
    conn.close()
