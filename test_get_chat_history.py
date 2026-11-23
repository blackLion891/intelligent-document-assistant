
from src.chat_repository import get_chat_history


# Step 1: Select document ID
document_id = 1

# Step 2: Retrieve chat history
history = get_chat_history(document_id)

# Step 3: Display history
print("\n========== PREVIOUS CHAT HISTORY ==========")

if not history:

    print("No chat history found for this PDF.")

else:

    for chat in history:

        print("\nChat ID:", chat["chat_id"])

        print("Document ID:", chat["document_id"])

        print("User Question:")
        print(chat["user_question"])

        print("\nAI Answer:")
        print(chat["ai_answer"])

        print("\nCreated At:", chat["created_at"])

        print("-----------------------------------")

print("\nChat history retrieval completed!")
