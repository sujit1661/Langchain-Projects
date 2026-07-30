# Docs: https://docs.langchain.com/oss/python/langchain/tools

import os
from typing import Type

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

# Pydantic models for tool arguments


class SimpleSearchInput(BaseModel):
    query: str = Field(description="should be a search query")


class MultiplyNumbersArgs(BaseModel):
    x: float = Field(description="First number to multiply")
    y: float = Field(description="Second number to multiply")


# Custom tool with only custom input
class SimpleSearchTool(BaseTool):
    # BaseTool is a Pydantic v2 model now, so class attributes need type
    # annotations (name/description used to work unannotated under Pydantic v1).
    name: str = "simple_search"
    description: str = "useful for when you need to answer questions about current events"
    args_schema: Type[BaseModel] = SimpleSearchInput

    def _run(
        self,
        query: str,
    ) -> str:
        """Use the tool."""
        from tavily import TavilyClient

        api_key = os.getenv("TAVILY_API_KEY")
        client = TavilyClient(api_key=api_key)
        results = client.search(query=query)
        return f"Search results for: {query}\n\n\n{results}\n"


# Custom tool with custom input and output
class MultiplyNumbersTool(BaseTool):
    name: str = "multiply_numbers"
    description: str = "useful for multiplying two numbers"
    args_schema: Type[BaseModel] = MultiplyNumbersArgs

    def _run(
        self,
        x: float,
        y: float,
    ) -> str:
        """Use the tool."""
        result = x * y
        return f"The product of {x} and {y} is {result}"


# Create tools using the Pydantic subclass approach
tools = [
    SimpleSearchTool(),
    MultiplyNumbersTool(),
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
print("Response for 'Search for Apple Intelligence':", run("Search for Apple Intelligence"))
print("Response for 'Multiply 10 and 20':", run("Multiply 10 and 20"))