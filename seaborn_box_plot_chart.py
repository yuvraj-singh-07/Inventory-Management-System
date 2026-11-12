from database import connect_database
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
def seaborn_box_plot_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT product_name, category, price FROM products""")
    data=cursor.fetchall()
    df=pd.DataFrame(data,columns=["Product","Category","Price"])
    sb.set_theme(style="dark",palette="deep",font_scale=1.2)
    fig=plt.figure(figsize=(11,6))
    fig.set_facecolor("#e542cd")
    ax=plt.gca()
    ax.set_facecolor("#052af9")
    sb.boxplot(data=df, x="Category", y="Price", color="orange",
               linewidth=2, saturation=0.8)
    plt.title("Category-wise Product Price Analysis")
    plt.xlabel("Category")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    cursor.close()
    conn.close()
