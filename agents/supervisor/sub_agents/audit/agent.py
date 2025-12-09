from google.adk.agents import Agent
from google.genai import types

print("✅ Libraries imported.")

audit = Agent(
model = "gemini-3-pro-preview",
    name = "audit",
    description = "",
    instruction = f"""

    """,
)
