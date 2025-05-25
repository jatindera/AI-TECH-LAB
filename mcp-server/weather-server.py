from fastmcp import FastMCP
import random

# Initialize the MCP server
mcp = FastMCP("Weather Server", host="localhost", port=8080)
# Define a tool for getting weather
@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a city"""
    # Mock weather data (replace with a real API in production)
    conditions = ["sunny", "cloudy", "rainy", "snowy"]
    weather = random.choice(conditions)
    temp = random.randint(10, 30)
    return f"The weather in {city} is {weather} with a temperature of {temp}°C."
# Add another tool for forecast

@mcp.tool()
def get_forecast(city: str, days: int) -> str:
    """Get a weather forecast for the next few days"""
    conditions = ["sunny", "cloudy", "rainy", "snowy"]
    forecast = [random.choice(conditions) for _ in range(days)]
    return f"Forecast for {city}: {', '.join(forecast)} for the next {days} days."

if __name__ == "__main__":
    mcp.run()