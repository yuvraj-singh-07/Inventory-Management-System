from database import connect_database
def add_product():
    conn,cursor = connect_database()
    product_name = input("Enter product Name : ")
    category = input("Enter category : ")
    price = float(input("Enter price : "))
    quantity = int(input("Enter quantity  : "))
    supplier = input("Enter supplier name : ")
    sql = """
INSERT INTO products(product_name, category, price, quantity, supplier)
values(%s, %s, %s, %s, %s)"""
    values = (product_name, category, price, quantity, supplier)
    cursor.execute(sql, values)
    conn.commit()
    print("\nProduct Added.")
    cursor.close()
    conn.close()