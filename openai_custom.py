from openai import OpenAI
from constants import OPENAI_API_KEY, OPENAI_MODEL

async def get_openai_response(query: str) -> str:
    """
    Get a response from OpenAI API.
    Args:
        query (str): The query to send to the OpenAI API.
    Returns:
        str: The response from the OpenAI API.
    """

    openai_client = OpenAI(api_key=OPENAI_API_KEY)
    response = openai_client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": query}]
    )
    return {
        "response": response.choices[0].message.content,
        "model": OPENAI_MODEL,
        "usage": response.usage.dict()
    }

