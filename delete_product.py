from database import connect_database
def delete_product():
    conn, cursor = connect_database()
    try:
        product_id = int(input("Enter Product Id : "))
        check_sql = "SELECT * FROM products WHERE product_id = %s"
        cursor.execute(check_sql, (product_id,))
        product = cursor.fetchone()

        if product is None:
            print("\nProduct Not Found")
            return

        print("\nCurrent product details")
        print("-" * 20)
        print("Product ID : ", product[0])
        print("Product Name : ", product[1])
        print("Category : ", product[2])
        print("Price : ", product[3])
        print("Quantity : ", product[4])
        print("Supplier : ", product[5])

        choice = input("\nDo you want to delete this product (yes/no)? ")
        if choice.strip().upper() == "YES":
            delete_sql = "DELETE FROM products WHERE product_id = %s"
            cursor.execute(delete_sql, (product_id,))
            conn.commit()
            print("\nProduct Deleted.")
        else:
            print("\nDelete cancelled.")
    finally:
        cursor.close()
        conn.close()
    
