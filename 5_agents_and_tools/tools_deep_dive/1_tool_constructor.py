# Docs: https://docs.langchain.com/oss/python/langchain/agents

from langchain.agents import create_agent
from langchain_core.tools import StructuredTool, Tool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


# Functions for the tools
def greet_user(name: str) -> str:
    """Greets the user by name."""
    return f"Hello, {name}!"


def reverse_string(text: str) -> str:
    """Reverses the given string."""
    return text[::-1]


def concatenate_strings(a: str, b: str) -> str:
    """Concatenates two strings."""
    return a + b


# Pydantic model for tool arguments
class ConcatenateStringsArgs(BaseModel):
    a: str = Field(description="First string")
    b: str = Field(description="Second string")


# Create tools using the Tool and StructuredTool constructor approach
tools = [

    # Use Tool for simpler functions with a single input parameter.
    # This is straightforward and doesn't require an input schema.
    Tool(
        name="GreetUser",  # Name of the tool
        func=greet_user,  # Function to execute
        description="Greets the user by name.",  # Description of the tool
    ),

    # Use Tool for another simple function with a single input parameter.
    Tool(
        name="ReverseString",  # Name of the tool
        func=reverse_string,  # Function to execute
        description="Reverses the given string.",  # Description of the tool
    ),

    # Use StructuredTool for more complex functions that require multiple input parameters.
    # StructuredTool allows us to define an input schema using Pydantic, ensuring proper validation and description.
    StructuredTool.from_function(
        func=concatenate_strings,  # Function to execute
        name="ConcatenateStrings",  # Name of the tool
        description="Concatenates two strings.",  # Description of the tool
        args_schema=ConcatenateStringsArgs,  # Schema defining the tool's input arguments
    ),
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