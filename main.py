from typing import List
from fastmcp import FastMCP

mcp: FastMCP = FastMCP("FastMCP Sandbox")


@mcp.tool()
def letter_counter(word: str, letter: str) -> int:
    """
    単語の中に文字が何個現れるかを数える

    Args:
        word: 分析する単語またはフレーズ
        letter: 出自限界すを数える文字

    Returns:
        単語中にその文字が現れる回数
    """
    return word.lower().count(letter.lower())


@mcp.tool()
def generate_uuid(n: int) -> List[str]:
    """
    UUIDをn個生成する

    Args:
        n: UUIDの数

    Returns:
        UUIDのリスト
    """
    import uuid6

    return [str(uuid6.uuid7()) for _ in range(n)]


if __name__ == "__main__":
    mcp.run(transport="stdio")
