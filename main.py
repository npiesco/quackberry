# /quackberry/main.py
from fastapi import FastAPI, Query as FastAPIQuery, HTTPException
from typing import List, Optional
import uvicorn
import nest_asyncio
import asyncio
from strawberry.fastapi import GraphQLRouter
from dotenv import load_dotenv
import os

# Project Specific Imports
from src.api.schemas import ExampleSchema
from src.data.dataaccess import read_delta
from src.graphql_api.graphql_schema import schema
from src.middleware.ratelimit import RateLimitMiddleware
from src.middleware.cors_middleware import add_cors_middleware
from src.utils.logging import setup_logging

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv()

# Logger setup
logger = setup_logging()

# FastAPI setup
app = FastAPI()

# Add CORS middleware
add_cors_middleware(app)

# Add rate limiting middleware
app.add_middleware(RateLimitMiddleware, max_requests=100, window_size=60)

# Define route to get example data
@app.get("/example", response_model=List[ExampleSchema])
async def get_example_data(
    start: int = FastAPIQuery(0, ge=0),
    limit: int = FastAPIQuery(100, ge=1, le=1000),
    filters: Optional[str] = None
):
    # Note: This allows for WHERE/AND clause style filtering by accepting dictionary of key-value pairs corresponding to field-value pairs
    filter_dict = {}
    if filters:
        filter_pairs = filters.split(',')
        for pair in filter_pairs:
            field, value = pair.split('=')
            filter_dict[field] = value
    try:
        data = read_delta(start, limit, filter_dict)
        return [ExampleSchema(**row) for row in data]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Add GraphQL route
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

def run_app():
    # Get SSL key and cert paths from .env file
    ssl_keyfile = os.getenv("SSL_KEY")
    ssl_certfile = os.getenv("SSL_CERT")
    
    # Configure and run server
    config = uvicorn.Config(
        app, 
        host="0.0.0.0", 
        port=8000, 
        log_level="info", 
        ssl_keyfile=ssl_keyfile, 
        ssl_certfile=ssl_certfile
    )
    # Start uvicorn server and asyncio event loop
    server = uvicorn.Server(config)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server.serve())

if __name__ == "__main__":
    run_app()