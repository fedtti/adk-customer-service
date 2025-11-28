from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types

print("✅ Libraries imported.")

from .sub_agents.agent.agent import agent
from .sub_agents.audit.agent import audit
from .sub_agents.nba.agent import nba

""" """
supervisor = Agent(
    model = LiteLlm(
        model = "ollama_chat/gemma3:latest",
        api_base = "http://localhost:11434",
    ),
    name = "supervisor",
    description = "Coordinate customers’ transfers to agents.",
    instruction = f"""
        You are an experienced customer service supervisor.
        Your task is to **coordinate customers’ transfers
        to agents**.

        You have specialized sub-agents:
          1. '{agent.name}' - Handles customers’ questions.
                              Delegate to it for ALL the customers’
                              questions. Don’t delegate to it ONLY
                              for greetings.
          2. '{audit.name}' - Handles auditing of '{agent.name}' answers
                              to the customers.
                              Delegate to it after EACH '{agent.name}'
                              answer.
          3. '{nba.name}'   - Handles special offers for the customers.
                              Delegate to it ONLY if a customer is
                              eligible for an offer from '{nba.name}'.

        For anything else, respond appropriately or state you cannot
        handle it.
    """,
    sub_agents = [
        agent,
        audit,
        nba
    ]
)

print(f"✅ Agent '{supervisor.name}' created using model '{supervisor.model.model}' with sub-agents: '{[sub_agent.name for sub_agent in supervisor.sub_agents]}'.")

root_agent = supervisor
