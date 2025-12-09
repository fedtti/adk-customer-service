from google.adk.agents import Agent
from google.genai import types

print("✅ Libraries imported.")

agent = Agent(
model = "gemini-3-pro-preview",
    name = "agent",
    description = "",
    instruction = f"""

    """,
)
