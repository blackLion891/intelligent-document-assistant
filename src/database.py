import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "root"),
            database=os.getenv("DB_NAME", "personal_pdf_chatbot"),
            port=int(os.getenv("DB_PORT", "3306"))
        )

        if connection.is_connected():
            print("MySQL database connected successfully!")

        return connection
    except mysql.connector.Error as error:
        print(f"MySQL connection failed: {error}")
        raise