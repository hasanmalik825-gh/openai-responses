# Import FastAPI and necessary packages
from fastapi import FastAPI,Query
import uvicorn
import logging
from openai_custom import get_openai_response
# Initialize FastAPI app
app = FastAPI()


@app.get("/")
async def index() -> dict:
    """
    Index route to check if the API is working.
    Returns:
        dict: The status of the API.
    """
    logging.info("Index is working")
    return {
        "Status": True,
        "message": "API is working.."
    }

@app.post("/response")
async def get_response(
    query: str = Query(..., description="write your query."),
) -> dict:
    logging.info(f"Query: {query}")
    return {
        "response":f"{await get_openai_response(query)}"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
