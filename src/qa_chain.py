from langchain_core.prompts import ChatPromptTemplate
from src.llm import get_groq_llm
from src.retriever import retrieve_relevant_chunks

def answer_question(vector_store, question):
    documents = retrieve_relevant_chunks(
        vector_store,
        question,
        k=3
    )
    if not documents:
        return "I could not find relevant information in the PDF."

    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """You are a PDF question-answering assistant.

            Answer the user's question using only the
            information provided in the PDF context.

            Do not use outside knowledge.
            Do not invent information.

            If the answer is not available in the context,
            say: "The answer is not available in the provided PDF."
            """
        ),
        (
            "human",
            """PDF Context:
            {context}

            User Question:
            {question}
            """   
        )
    ])

    llm = get_groq_llm()

    chain = prompt | llm

    response = chain.invoke({
        "context": context,
        "question": question
    })

    return response.content