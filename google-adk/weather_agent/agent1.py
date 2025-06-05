import os
from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams, StdioServerParameters
import asyncio
from google.adk.runners import Runner


load_dotenv()

# Connect to MCP Server
server_params = SseServerParams(url="http://0.0.0.0:8080/mcp")
mcp_toolset = MCPToolset(connection_params=server_params)

async def get_tools_async():
    """Get tools from weather MCP server"""
    tools, exit_stack = MCPToolset(connection_params=server_params)
    return tools, exit_stack

# --- Step 1: Agent Definition ---
async def get_agent_async():
    """creates an ADK agent equipped with tools from the MCP Server"""
    tools, exit_stack = await get_tools_async()
    print(f"Fetechted {len(tools)} tools from MCP Server.")
    root_agent = LlmAgent(
        name="WeatherAssistant",
        description="An ADK Agent equipped with tools from the MCP Server.",
        instruction="You help users by calling weather tools via MCP.",
        model="gemini-2.0-flash",
        tools=tools
    )
    return root_agent, exit_stack

# --- Step 2: Main Execution Logic ---
async def async_main():
  
  root_agent, exit_stack = await get_agent_async()

  runner = Runner(
      app_name='mcp_MCPWeatherAppfilesystem_app',
      agent=root_agent
  )

  # Crucial Cleanup: Ensure the MCP server process connection is closed.
  print("Closing MCP server connection...")
  await exit_stack.aclose()
  print("Cleanup complete.")


if __name__ == '__main__':
  try:
    asyncio.run(async_main())
  except Exception as e:
    print(f"An error occurred: {e}")
