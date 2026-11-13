from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """_summary_
        Get the weather for a location
    """
    return "It is always rainy in New Delhi."


if __name__ == "__main__":
    mcp.run(transport="streamable-http")

# streamable-http is a transport that allows to run as an API services itself.
# It allows you to make HTTP requests to the MCP server and get the response.
# It is a good transport for running the MCP server as a API service.

