# Documentation: https://docs.langchain.com/oss/python/langchain/agents

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


# Simple Tool with one parameter without args_schema
# This is a basic tool that does not require an input schema.
# Use this approach for simple functions that need only one parameter.
def greet_user(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}!"


# Pydantic models for tool arguments
# Define a Pydantic model to specify the input schema for tools that need more structured input.
class ReverseStringArgs(BaseModel):
    text: str = Field(description="Text to be reversed")


# Tool with One Parameter using args_schema
# Use the args_schema parameter to specify the input schema using a Pydantic model.
@tool(args_schema=ReverseStringArgs)
def reverse_string(text: str) -> str:
    """Reverses the given string."""
    return text[::-1]


# Another Pydantic model for tool arguments
class ConcatenateStringsArgs(BaseModel):
    a: str = Field(description="First string")
    b: str = Field(description="Second string")


# Tool with Two Parameters using args_schema
# This tool requires multiple input parameters, so we use the args_schema to define the schema.
@tool(args_schema=ConcatenateStringsArgs)
def concatenate_strings(a: str, b: str) -> str:
    """Concatenates two strings."""
    print("a", a)
    print("b", b)
    return a + b


# Create tools using the @tool decorator
# The @tool decorator simplifies the process of defining tools by handling the setup automatically.
tools = [
    greet_user,  # Simple tool without args_schema
    reverse_string,  # Tool with one parameter using args_schema
    concatenate_strings,  # Tool with two parameters using args_schema
]

# Initialize a ChatOpenAI model
llm = ChatOpenAI(model="gpt-4o")

# Create the agent. create_agent replaces both create_tool_calling_agent
# and AgentExecutor - it builds a tool-calling loop on top of LangGraph,
# so there's no separate "pull a prompt from the hub + wrap in an executor"
# step needed. A plain system prompt string is enough here.
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful assistant that can use tools to answer the user's request.",
)


def run(query: str):
    """Invoke the agent with a single user query and return the final text response."""
    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
    # The final AI message is the last one in the returned message list
    return result["messages"][-1].content


# Test the agent with sample queries
print("Response for 'Greet Alice':", run("Greet Alice"))
print("Response for 'Reverse the string hello':", run("Reverse the string 'hello'"))
print("Response for 'Concatenate hello and world':", run("Concatenate 'hello' and 'world'"))