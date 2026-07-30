import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_chroma import Chroma
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# Load environment variables from .env file
load_dotenv()

# Load the existing Chroma vector store
current_dir = os.path.dirname(os.path.abspath(__file__))
db_dir = os.path.join(current_dir, "..", "..", "4_rag", "db")
persistent_directory = os.path.join(db_dir, "chroma_db_with_metadata")

if not os.path.exists(persistent_directory):
    raise FileNotFoundError(
        f"The directory {persistent_directory} does not exist. Please check the path."
    )

print("Loading existing vector store...")

# Define the embedding model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Load the existing vector store with the embedding function
db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embeddings,
)

# Create a retriever for querying the vector store
retriever = db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)

# Create the chat model
llm = ChatOpenAI(model="gpt-4o")


# Wrap the retriever as a tool the agent can call.
# create_agent's built-in ReAct-style loop handles history-aware
# reformulation on its own (it sees the full message history each turn),
# so there's no need for a separate "history aware retriever" chain.
@tool
def retrieve_context(query: str) -> str:
    """Retrieve relevant document snippets to help answer a question about the context."""
    docs = retriever.invoke(query)
    if not docs:
        return "No relevant documents found."
    return "\n\n".join(
        f"[Source {i+1}]\n{doc.page_content}" for i, doc in enumerate(docs)
    )


system_prompt = (
    "You are an assistant for question-answering tasks. Use the "
    "retrieve_context tool to look up relevant information before "
    "answering. If you don't know the answer after retrieving context, "
    "just say that you don't know. Use three sentences maximum and keep "
    "the answer concise."
)

# Build the agent (runs on LangGraph under the hood)
agent = create_agent(
    model=llm,
    tools=[retrieve_context],
    system_prompt=system_prompt,
)

# Message history is just a plain list of role/content dicts now
messages = []
while True:
    query = input("You: ")
    if query.lower() == "exit":
        break

    messages.append({"role": "user", "content": query})
    result = agent.invoke({"messages": messages})

    # result["messages"] is the full updated conversation; take the last AI message
    ai_message = result["messages"][-1]
    print(f"AI: {ai_message.content}")

    # Keep full history (including any tool calls) for context in next turn
    messages = result["messages"]
