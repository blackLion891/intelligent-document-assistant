
from src.database import get_db_connection


def save_pdf_details(filename, file_path, total_pages):

    connection = None
    cursor = None

    try:
        # Step 1: Connect to MySQL
        connection = get_db_connection()

        cursor = connection.cursor()

        # Step 2: Insert PDF details
        query = """
            INSERT INTO pdf_documents
            (filename, file_path, total_pages)
            VALUES (%s, %s, %s)
        """

        values = (filename, file_path, total_pages)

        cursor.execute(query, values)

        # Step 3: Save changes
        connection.commit()

        # Step 4: Get generated document ID
        document_id = cursor.lastrowid

        print("PDF details saved successfully!")

        return document_id

    except Exception as error:

        if connection and connection.is_connected():
            connection.rollback()

        print("Error saving PDF details:", error)
        raise

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

def get_all_documents():

    from src.database import get_db_connection

    connection = None
    cursor = None

    try:
        # Step 1: Connect to MySQL
        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        # Step 2: Retrieve PDF details
        query = """
            SELECT
                document_id,
                filename,
                file_path,
                total_pages,
                uploaded_at
            FROM pdf_documents
            ORDER BY uploaded_at DESC, document_id DESC
        """

        cursor.execute(query)

        # Step 3: Fetch all documents
        documents = cursor.fetchall()

        print("PDF documents retrieved successfully!")

        return documents

    except Exception as error:

        print("Error retrieving PDF documents:", error)
        raise

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
