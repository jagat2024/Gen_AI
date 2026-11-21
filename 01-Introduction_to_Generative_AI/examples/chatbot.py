
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()


# Initialize model
def get_model():
    return init_chat_model(
        "openai/gpt-oss-120b",
        model_provider="groq",
        temperature=0.7,
    )


model = get_model()


# Select AI personality
print("\n========== CHOOSE YOUR AI MODE ==========")
print("1. Angry Mode 😡")
print("2. Funny Mode 😂")
print("3. Sad Mode 😢")

choice = int(input("\nChoose your mode: "))


if choice == 1:
    mode = "You are an angry AI assistant. Respond aggressively and impatiently, but never use abusive language."

elif choice == 2:
    mode = "You are a very funny AI assistant. Respond with humor, jokes and witty comments."

elif choice == 3:
    mode = "You are a sad AI assistant. Respond in a sad, emotional and melancholic tone."

else:
    print("Invalid choice!")
    exit()


# Initialize chat history
messages = [
    SystemMessage(content=mode)
]


print("\n========== AI CHATBOT ==========")
print("Type 0 to exit the application.\n")


# Chat loop
while True:

    prompt = input("You: ")

    if prompt == "0":
        print("Chatbot: Goodbye!")
        break

    # Add user message
    messages.append(HumanMessage(content=prompt))

    # Generate response
    response = model.invoke(messages)

    # Store AI response
    messages.append(AIMessage(content=response.content))

    print("Bot:", response.content)


print("\n========== CHAT HISTORY ==========")
for message in messages:
    print(f"{message.type}: {message.content}")
