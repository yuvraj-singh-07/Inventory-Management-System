from database import connect_database
def update_product():
    conn,cursor = connect_database()
    product_id = int(input("Enter product Id : "))
    check_sql="SELECT * FROM products WHERE product_id = %s"
    cursor.execute(check_sql, (product_id,))
    product=cursor.fetchone()
    if product is None:
        print("\nProduct Not Found")
    else:
        print("\nCurrent product details")
        print("-"*20)
        print("Product Name : ",product[1])
        print("category : ",product[2])
        print("Price : ",product[3])
        print("Quantity : ",product[4])
        print("Supplier : ",product[5])
        new_price=float(input("\n Enter the price : "))
        new_quantity=int(input("\nEnter New Quantity : "))
        update_sql="""UPDATE products SET price=%s,quantity=%s WHERE product_id=%s"""
        cursor.execute(update_sql, (new_price, new_quantity, product_id))
        conn.commit()
        print("\nProduct updated successfully.")
    cursor.close()
    conn.close()
