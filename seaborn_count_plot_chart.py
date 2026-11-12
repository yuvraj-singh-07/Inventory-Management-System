from database import connect_database
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
def seaborn_count_plot_chart():
    conn,cursor=connect_database()
    cursor.execute("""SELECT product_name, category FROM products""")
    data=cursor.fetchall()
    df = pd.DataFrame(data,columns=["Product","Category"])
    sb.set_theme(style="ticks",palette="pastel",font_scale=1.1)
    fig=plt.figure(figsize=(10,6))
    fig.set_facecolor("#b48395")
    ax=plt.gca()
    ax.set_facecolor("#b22395")
    sb.countplot(data=df, y="Category", linewidth=2, width=0.6,
                 edgecolor="#055B05", saturation=1)
    plt.title("Category Wise Product Count",fontsize=16,fontweight="bold")
    plt.xlabel("Total Products",fontsize=12)
    plt.ylabel("Category",fontsize=12)
    plt.xticks(rotation=15)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    cursor.close()
    conn.close()
