import os
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
import openai

CHROMA_PATH = "chroma"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

openai.api_key = OPENAI_API_KEY


def load_documents(data_path):
    loader = DirectoryLoader(
        data_path,
        glob="**/*.txt"
    )
    documents = loader.load()
    print(f"Found {len(documents)} documents")
    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Now have {len(chunks)} chunks")
    return chunks


def create_chroma_db(chunks):
    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    if not os.path.exists(CHROMA_PATH) or not os.listdir(CHROMA_PATH):
        db = Chroma.from_documents(
            chunks,
            embedding,
            persist_directory=CHROMA_PATH
        )
        print("Creating new Chroma DB.")
    else:
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding)
        print("Loading existing Chroma DB.")
    return db


def query_chroma(db, query_text, top_k=3, relevance_threshold=0.7):
    results = db.similarity_search_with_score(query_text, k=top_k)

    if not results:
        print("No results found.")
        return []

    filtered_results = []
    for doc, score in results:
        if score > relevance_threshold:
            filtered_results.append(doc)
        else:
            print(f"Low relevance score: {score:.2f} (below threshold of {relevance_threshold:.2f})")

    if not filtered_results:
        print(f"No results with relevance score above {relevance_threshold:.2f} found.")
        return []

    context_text = "\n\n---\n\n".join([doc.page_content for doc in filtered_results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = ChatOpenAI()
    response_text = model.predict(prompt)

    sources = [doc.metadata.get("source", None) for doc in filtered_results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    return formatted_response


if __name__ == '__main__':
    data_path = 'data'
    documents = load_documents(data_path)
    chunks = split_documents(documents)
    db = create_chroma_db(chunks)
    # query_string = input("Enter your query: ")
    query_string = "How does Alice meet the Mad Hatter ?"
    response = query_chroma(db, query_string, relevance_threshold=0.2)
    print(response)
