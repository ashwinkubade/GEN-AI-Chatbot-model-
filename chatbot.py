from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.7
)
message=[
    SystemMessage(content="You are a fuuny AI agent."),
    
]
print(">>> Welcome to the Mistral AI Chatbot! Type 0 to quit.")
while True:
    prompt = input("you: ")
    message.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("bot:", response.content)
print(message)

