from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

root_agent = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "audit",
    description = "",
    instruction = """
        You are an experienced customer service operator that audits other operators.
    """,
)