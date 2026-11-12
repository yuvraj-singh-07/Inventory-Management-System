from database import connect_database
def search_product():
    conn, cursor=connect_database()
    search_name = input("Enter product name : ")
    sql=""" SELECT * FROM products WHERE product_name LIKE %s"""
    values = ("%" + search_name + "%",)
    cursor.execute(sql, values)
    products=cursor.fetchall()
    if len(products)==0:
        print("\nProduct Not Found")
    else:
        print("\n" + "="*90)
        print("{:<5} {:<20} {:<15} {:<12} {:<10} {:<20}".format(
            "ID", "Product Name", "Category", "Price", "Qty", "Supplier"
        ))
        print("="*90)
        for product in products:
            print("{:<5} {:<20} {:<15} {:<12} {:<10} {:<20}".format(
                product[0], product[1], product[2], product[3], product[4], product[5]
            ))
    cursor.close()
    conn.close()
