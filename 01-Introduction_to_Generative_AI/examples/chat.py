
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    temperature=0.7,
)

response = model.invoke("Explain Machine Learning")

print(response.content)
