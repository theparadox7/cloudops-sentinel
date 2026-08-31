from app.db.connection import get_connection


connection = get_connection()

try:
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    result = cursor.fetchone()

    print("Database connection successful!")
    print(result)

    cursor.close()
finally:
    connection.close()