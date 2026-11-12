from database import connect_database
def view_product():
    conn,cursor=connect_database()
    sql="SELECT * FROM products"
    cursor.execute(sql)
    products=cursor.fetchall()
    if len(products)==0:
        print("\nNo Product Found")
    else:
        print("\n" + "="*90)
        print("{:<5} {:<20} {:<15} {:<12} {:<10} {:<20}".format("ID","Product_Name","Category","Price","Qty","Supplier"))
        print("="*90)
        for product in products:
            print("{:<5} {:<20} {:<15} {:<12} {:<10} {:<20}".format(
                product[0], product[1], product[2], product[3], product[4], product[5]
            ))
            print("="*90)
    cursor.close()
    conn.close()
