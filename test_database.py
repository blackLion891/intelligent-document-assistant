from src.database import get_db_connection


try:
    # Step 1: Connect to MySQL
    connection = get_db_connection()

    # Step 2: Create cursor
    cursor = connection.cursor()

    # Step 3: Check database name
    cursor.execute("SELECT DATABASE()")

    result = cursor.fetchone()

    print("\nConnected Database:", result[0])

    # Step 4: Check existing tables
    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    print("\nAvailable Tables:")

    for table in tables:
        print(table[0])

    print("\nDatabase testing completed successfully!")

except Exception as error:
    print("Database testing failed:", error)

finally:
    if "cursor" in locals():
        cursor.close()

    if "connection" in locals() and connection.is_connected():
        connection.close()
        print("\nMySQL connection closed.")
