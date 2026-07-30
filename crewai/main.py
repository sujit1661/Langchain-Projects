from crewai import Crew,Agent,Task,Process
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
llm_1 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)

llm_2 = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.3
)



researcher=Agent(
    role="researcher",
    goal="Find accurate and latest information on a topic",
    backstory="Expert in research and data gathering",
    llm=llm_1,
    verbose=True
)


writer=Agent(
    role="writer",
    goal="Write engaging and structured blog content",
    backstory="Professional blog writer",
    llm=llm_2,
    verbose=True
)


topic=input("topic: ")

task1=Task(
    description=f"Research the topic: {topic}. Find key points, facts, and trends",
    expected_output="bullet points structure",
    agent=researcher,
)

task2 = Task(
    description=f"Write a detailed blog on: {topic} using the research.",
    expected_output="Well-structured blog with headings",
    agent=writer
)


crew=Crew(
    agents=[researcher,writer],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True
)


result=crew.run()
print("\n\n🔥 FINAL OUTPUT:\n")
print(result)