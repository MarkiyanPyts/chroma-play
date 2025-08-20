import chromadb
chroma_client = chromadb.Client()
from chromadb.utils import embedding_functions

default_ef = embedding_functions.DefaultEmbeddingFunction()

collection_name = "test_collection"
collection = chroma_client.get_or_create_collection(name=collection_name, embedding_function=default_ef)

documents = [
    {"id": "doc1", "text": "Hello, world!"},
    {"id": "doc2", "text": "How are you today?"},
    {"id": "doc3", "text": "Goodbye, see you later!"},
    {
        "id": "doc4",
        "text": "Microsoft is a technology company that develops software. It was founded by Bill Gates and Paul Allen in 1975.",
    },
]

for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

query = "Hello, world !"

results = collection.query(query_texts=[query], n_results=2)

print(results)

for idx, documents in enumerate(results["documents"][0]):
    print(f"Document {idx}:")
    doc_id = results['ids'][0][idx]
    distance = results['distances'][0][idx]
    print(f"For the query '{query}', found document {doc_id} with a distance of {distance}.")