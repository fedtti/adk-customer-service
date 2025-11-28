from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types

""" """
audit = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "audit",
    description = "Audits other agents’ answers.",
    instruction = """
        You are an experienced customer service agent.
        Your ONLY task is to **audit other agents’ answers**.
    """
)
