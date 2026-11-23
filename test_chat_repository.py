
from src.chat_repository import save_chat_history


# Step 1: Select existing document ID
document_id = 1

# Step 2: User question
user_question = "What is Artificial Intelligence?"

# Step 3: Example AI answer
ai_answer = """
Artificial Intelligence (AI) is a technology
that enables machines to perform tasks
that normally require human intelligence.
"""

# Step 4: Save chat history
chat_id = save_chat_history(
    document_id=document_id,
    user_question=user_question,
    ai_answer=ai_answer
)

# Step 5: Display results
print("\n========== CHAT HISTORY ==========")

print("Chat ID:", chat_id)
print("Document ID:", document_id)
print("User Question:", user_question)
print("AI Answer:", ai_answer)

print("\nChat history testing completed!")
