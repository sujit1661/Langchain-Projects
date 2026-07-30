from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def get_current_time() -> str:
    """Returns the current time in H:MM AM/PM format."""
    import datetime

    return datetime.datetime.now().strftime("%I:%M %p")


@tool
def search_wikipedia(query: str) -> str:
    """Search Wikipedia and return a short summary."""
    from wikipedia import summary

    try:
        return summary(query, sentences=2)
    except Exception:
        return "I couldn't find any information on that."


llm = ChatOpenAI(model="gpt-4o")

agent = create_agent(
    model=llm,
    tools=[get_current_time, search_wikipedia],
    system_prompt=(
        "You are a helpful AI assistant. "
        "Use the available tools whenever they help answer the user's question."
    ),
)

while True:
    user_input = input("User: ")

    if user_input.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        }
    )

    print("Bot:", response["messages"][-1].content)