import mysql.connector


def connect_database():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="yuviii_x",
        database="Inventory_Management",
    )
    cursor = conn.cursor()
    return conn,cursor
