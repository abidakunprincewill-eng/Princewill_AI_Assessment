from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="chroma_db_local",
    embedding_function=embeddings
)

# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# Retrieve relevant information
def retrieve_information(question):
    results = retriever.invoke(question)
    return results


# Test the retriever
if __name__ == "__main__":
    question = input("Ask Ledgerly a question: ")

    documents = retrieve_information(question)

    if not documents:
        print("No relevant information found.")

    for i, document in enumerate(documents, 1):
        print(f"\n--- Result {i} ---")
        print(document.page_content)
        print("Source:", document.metadata.get("source"))