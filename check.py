from database import connect_database
conn,cursor = connect_database()
print("Database Connected Successfully")
cursor.close()
conn.close()
