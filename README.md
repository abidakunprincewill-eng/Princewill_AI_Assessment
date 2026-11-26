Good day Mr Maro Sir. it took me a week to get jus this 40% done. i please request more time 
because it is running me mad

Ledgerly – AI Help Desk Assistant

Ledgerly is an AI-powered customer support assistant designed to answer customer questions using information retrieved from a company knowledge base.

Project Overview

The project uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from company documents and use it to generate helpful responses.

Technologies

- Python
- LangChain
- Hugging Face Embeddings
- ChromaDB
- Streamlit (user interface – in development)
ollama model
Current Features

- Loading company knowledge-base documents.
- Splitting documents into smaller text chunks.
- Generating embeddings locally using Hugging Face.
- Storing document embeddings in ChromaDB.
- Retrieving relevant information based on user questions.

Project Structure

Princewill_AI_Assessment/
├── data/
├── chroma_db_local/
├── app.py
├── ingest.py
├── retriever.py
├── requirements.txt
├── README.md
└── .gitignore

Running the Project

1. Clone the repository.

2. Install the dependencies:
   
   "pip install -r requirements.txt"

3. Build the knowledge base:
   
   "python ingest.py"

4. Test document retrieval:
   
   "python retriever.py"

Development Status

Document ingestion and retrieval are implemented. AI answer generation, source citations, fallback responses, and the Streamlit interface are still under development.

Author

Princewill
