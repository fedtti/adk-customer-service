from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

print("✅ Libraries imported.")

""" """
agent = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "agent",
    description = "Answers users’ questions",
    instruction = f"""
        You help users with their problems.
    """,
    tools = []
)

print(f"✅ Agent '{agent.name}' created using model '{agent.model.model}'.")

root_agent = agent
