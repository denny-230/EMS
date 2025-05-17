import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        username='root',
        password='Test@123',
        database='new_data'
    )
    print("Connected Successfully!")
except Exception as e:
    print("Connection Failed:", e)
