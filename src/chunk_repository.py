
from src.database import get_db_connection


def save_pdf_chunks(document_id, chunks):

    if not chunks:
        raise ValueError("No PDF chunks available!")

    connection = None
    cursor = None

    try:
        # Step 1: Connect to MySQL
        connection = get_db_connection()
        cursor = connection.cursor()

        # Step 2: Prepare SQL query
        query = """
            INSERT INTO pdf_chunks
            (document_id, chunk_text, page_number)
            VALUES (%s, %s, %s)
        """

        # Step 3: Prepare chunk data
        values = []

        for chunk in chunks:

            page_number = chunk.metadata.get("page")

            if page_number is not None:
                page_number = int(page_number) + 1

            values.append((
                document_id,
                chunk.page_content,
                page_number
            ))

        # Step 4: Insert all chunks
        cursor.executemany(query, values)

        # Step 5: Save changes
        connection.commit()

        print(f"{cursor.rowcount} PDF chunks saved successfully!")

        return cursor.rowcount

    except Exception as error:

        if connection and connection.is_connected():
            connection.rollback()

        print("Error saving PDF chunks:", error)
        raise

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
