from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"  
)
print("Model loaded successfully!")
texts=[
    "Hello my name is jagat..",
    "hello your name is youtube",
    "and you all are very beautiful"
]
vector = embedding.embed_documents(texts)

print("Total embeddings:", len(vector))
print("Dimensions:", len(vector[0]))

print("First vector:", vector[0])
