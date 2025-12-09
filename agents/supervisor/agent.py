from google.adk.agents import Agent
# from google.adk.runners import Runner
# from google.adk.sessions import InMemorySessionService
from google.genai import types

print("✅ Libraries imported.")

from .sub_agents.agent import agent as agent
from .sub_agents.audit import agent as audit

print("✅ Agents imported.")

""" """
supervisor = Agent(
    model = "gemini-3-pro-preview",
    name = "supervisor",
    description = "Supervise agents’ activities",
    instruction = f"""
        You are an experienced customer service supervisor.
        Your role is to supervise agents’ activities.

        You have two specialized sub-agents:
        1. '{agent.agent.name}': Handles users’ questions. Delegate to it if the user asks a question.
        2. '{audit.audit.name}': Handles agent’s answers. Delegate to it after '{agent.agent.name}' answered the user question.

        You also have a tool:
        - '': 

        For anything else, respond appropriately or state you cannot handle it.
    """,
    sub_agents = [
        agent,
        audit
    ],
    tools = [
      
    ]
)

print(f"✅ Agent '{supervisor.name}' created using model '{supervisor.model}' with sub-agents: {[]}, and tools: {[]}.")

root_agent = supervisor # Export for ADK.
