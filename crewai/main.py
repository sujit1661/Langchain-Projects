from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/openai/gpt-oss-20b",
    temperature=0.3,
)

researcher = Agent(
    role="Researcher",
    goal="Research the given topic",
    backstory="Expert researcher",
    llm=llm,
    verbose=True,
)

writer = Agent(
    role="Writer",
    goal="Write a blog",
    backstory="Professional content writer",
    llm=llm,
    verbose=True,
)

task1 = Task(
    description="Research AI Agents",
    expected_output="Bullet points",
    agent=researcher,
)

task2 = Task(
    description="Write a blog using the research.",
    expected_output="A complete blog",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    process=Process.sequential,
)

result = crew.kickoff()
print(result)