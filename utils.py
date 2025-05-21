import os
import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.agents import Agent
from google.genai import types

async def call_agent(agent: Agent, message_text: str) -> str:
    """
    Sends a message to an agent via Runner and returns the final response.
    This function now correctly handles the asynchronous execution of ADK Runner
    within an existing event loop (like FastAPI's).
    """
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=agent.name, user_id="user1", session_id="session1")
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=message_text)])
    final_response_parts = []
    loop = asyncio.get_running_loop()

    # Run the synchronous runner.run() iterator in a separate thread.
    # This prevents blocking the main event loop and avoids nested asyncio.run() issues.
    # We convert the async generator to a list in the executor thread to exhaust it.
    events = await loop.run_in_executor(
        None, # Use the default ThreadPoolExecutor
        lambda: list(runner.run(user_id="user1", session_id="session1", new_message=content))
    )

    for event in events:
        if event.is_final_response():
            for part in event.content.parts:
                if part.text is not None:
                    final_response_parts.append(part.text)
    
    # Join all parts and strip any leading/trailing whitespace including newlines
    return "".join(final_response_parts).strip()
