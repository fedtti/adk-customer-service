from google.adk.agents import Agent
from google.genai import types

print("✅ Libraries imported.")

""" """
supervisor = Agent(
    name = "supervisor",
    description = "Answers users’ questions",
    instruction = f"""
        You are an experienced customer service agent.
        Your ONLY task is to answer users’ question. Do nothing else.
    """,
)

print(f"✅ .")