# Add lifespan support for startup/shutdown with strong typing

from bilibili_api import search, sync
from mcp.server.fastmcp import Context, FastMCP

# Create a named server
mcp = FastMCP("Bilibili Mcp Server")


# Access type-safe lifespan context in tools


@mcp.tool()
def generate_search(query: str) -> dict:
    """根据提供的问题搜索Bilibili平台，并返回搜索结果

    Args:
        query (str): 需要在Bilibili平台搜索的问题

    Returns:
        dict: 从Bilibili平台搜索结果中提取的信息
    """

    return sync(search.search_by_type(keyword=query, search_type=search.SearchObjectType.VIDEO))


@mcp.tool()
def get_hot_news() -> dict:
    """获取Bilibili平台目前的热搜新闻

    Args:

    Returns:
        dict: Bilibili平台目前的热搜新闻
    """

    return sync(search.get_hot_search_keywords())


if __name__ == "__main__":
    mcp.run(transport='stdio')
