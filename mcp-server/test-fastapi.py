from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from pydantic import BaseModel
import random
import requests, uuid, json, os
from dotenv import find_dotenv, load_dotenv

app = FastAPI()
load_dotenv(find_dotenv())

# Take the FastAPI app only as a source for MCP server generation
mcp = FastApiMCP(
    app,
    name = "MCP Implementation",
    describe_all_responses=True,
    describe_full_response_schema=True
    )
# Mount the MCP server to a separate FastAPI app
mcp.mount()

# Define a tool for getting weather
@app.post("/get-weather", operation_id="get_weather")
def get_weather(city: str) -> str:
    """Get the current weather for a city"""
    # Mock weather data (replace with a real API in production)
    conditions = ["sunny", "cloudy", "rainy", "snowy"]
    weather = random.choice(conditions)
    temp = random.randint(10, 30)
    return f"The weather in {city} is {weather} with a temperature of {temp}°C."
# Add another tool for forecast

@app.post("/weather-forecast", operation_id="weather_forecast")
def get_forecast(city: str, days: int) -> str:
    """Get a weather forecast for the next few days"""
    conditions = ["sunny", "cloudy", "rainy", "snowy"]
    forecast = [random.choice(conditions) for _ in range(days)]
    return f"Forecast for {city}: {', '.join(forecast)} for the next {days} days."

# Run the MCP server separately from the original FastAPI app.
# It still works 🚀
# Your original API is **not exposed**, only via the MCP server.
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)


#     from fastmcp import FastMCP
# import random

# # Initialize the MCP server
# mcp = FastMCP("Weather Server", host="localhost", port=8080)

# # Define a tool for getting weather
# @mcp.tool()
# def get_weather(city: str) -> str:
#     """Get the current weather for a city"""
#     # Mock weather data (replace with a real API in production)
#     conditions = ["sunny", "cloudy", "rainy", "snowy"]
#     weather = random.choice(conditions)
#     temp = random.randint(10, 30)
#     return f"The weather in {city} is {weather} with a temperature of {temp}°C."
# # Add another tool for forecast

# @mcp.tool()
# def get_forecast(city: str, days: int) -> str:
#     """Get a weather forecast for the next few days"""
#     conditions = ["sunny", "cloudy", "rainy", "snowy"]
#     forecast = [random.choice(conditions) for _ in range(days)]
#     return f"Forecast for {city}: {', '.join(forecast)} for the next {days} days."
# if __name__ == "__main__":
#     mcp.run()