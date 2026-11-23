
from src.database import get_db_connection


def save_chat_history(document_id, user_question, ai_answer):

    connection = None
    cursor = None

    if not user_question or not user_question.strip():
        raise ValueError("User question cannot be empty!")

    if not ai_answer or not ai_answer.strip():
        raise ValueError("AI answer cannot be empty!")

    try:
        # Step 1: Connect to MySQL
        connection = get_db_connection()
        cursor = connection.cursor()

        # Step 2: Insert chat history
        query = """
            INSERT INTO chat_history
            (document_id, user_question, ai_answer)
            VALUES (%s, %s, %s)
        """

        values = (
            document_id,
            user_question,
            ai_answer
        )

        cursor.execute(query, values)

        # Step 3: Commit changes
        connection.commit()

        # Step 4: Get generated chat ID
        chat_id = cursor.lastrowid

        print("Chat history saved successfully!")

        return chat_id

    except Exception as error:

        if connection and connection.is_connected():
            connection.rollback()

        print("Error saving chat history:", error)
        raise

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()

def get_chat_history(document_id):

    connection = None
    cursor = None

    try:
        # Step 1: Connect to MySQL
        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        # Step 2: Retrieve chat history
        query = """
            SELECT
                chat_id,
                document_id,
                user_question,
                ai_answer,
                created_at
            FROM chat_history
            WHERE document_id = %s
            ORDER BY created_at ASC, chat_id ASC
        """

        cursor.execute(query, (document_id,))

        # Step 3: Fetch records
        history = cursor.fetchall()

        print("Chat history retrieved successfully!")

        return history

    except Exception as error:

        print("Error retrieving chat history:", error)
        raise

    finally:

        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
