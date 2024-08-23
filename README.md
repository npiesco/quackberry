# QuackBerry API Framework
<div align="center">
<img src="https://github.com/npiesco/svg-assets/blob/main/quackberry-logo.png?raw=true" alt="QuackBerry API Framework Logo" width="200">
</div>
A containerized modern, scalable, and asynchronous API framework with GraphQL support, leveraging Docker, FastAPI, Strawberry, Pydantic, DuckDB, Starlette, and Uvicorn.
## Architecture Diagram
<div align="center">
<img src="https://github.com/npiesco/svg-assets/blob/main/ArchitectureAPI.png?raw=true" alt="QuackBerry API Framework Architecture" width="1250">
</div>

## Features

- Containerized application using Docker for ease of deployment and scalability
- GraphQL support using Strawberry
- REST API endpoints using FastAPI
- Type definitions and validation using Pydantic
- Data access and querying using DuckDB
- Asynchronous functionality with Uvicorn
- CORS middleware for handling cross-origin requests
- Starlette for rate limiting middleware for protecting against excessive requests
- Logging utility for application logging

## Project Structure

```
Project Directory: /quackberry
- requirements.txt
- Dockerfile
- .env
- main.py
+ src/
|  + middleware/
|  |  - cors_middleware.py
|  |  - __init__.py
|  |  - ratelimit.py
|  + utils/
|  |  - logging.py
|  |  - __init__.py
|  + graphql_api/
|  |  + types/
|  |  |  - example_type.py
|  |  |  - example_sql_type.py
|  |  + queries/
|  |  |  - example_query.py
|  |  |  - example_sql_query.py
|  |  - __init__.py
|  |  - graphql_schema.py
|  + api/
|  |  - __init__.py
|  |  - schemas.py
|  + data/
|  |  - dataaccess.py
|  |  - __init__.py
```

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/your-username/quackberry.git
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the environment variables in the `.env` file.
   ```
   SSL_KEY=/path/to/your/ssl_key.pem
   SSL_CERT=/path/to/your/ssl_cert.pem
   DELTA_TABLE_PATHS=/path/to/delta_table
   ```
   
4. Run the application:
   ```
   python main.py
   ```

   The application will be accessible at `http://localhost:8000`, and the GraphQL endpoint will be available at `http://localhost:8000/graphql`.

## REST API Endpoints

- `/example`: Retrieve example data with pagination and filtering support.
  - Query Parameters:
    - `start` (optional): The starting index of the data (default: 0).
    - `limit` (optional): The maximum number of items to retrieve (default: 100, max: 1000).
    - `filters` (optional): Field-value pairs for filtering the data (format: `field1=value1,field2=value2`).

## GraphQL Queries

- `exampleQuery`: Retrieve example data with filtering support.
  - Arguments:
    - `start` (optional): The starting index of the data (default: 0).
    - `limit` (optional): The maximum number of items to retrieve (default: 100).
    - `filters` (optional): Field-value pairs for filtering the data (format: `field1=value1,field2=value2`).

## Customization

- Update the Pydantic schemas in `src/api/schemas.py` to define your API request/response models.
- Modify the data access functions in `src/data/dataaccess.py` to interact with your database or data source.
- Define your GraphQL types in `src/graphql_api/types/` and implement the corresponding queries in `src/graphql_api/queries/`.
- Customize the Starlette middleware in `src/middleware/` to add additional functionality or modify existing behaviors.

## Deployment

The application is containerized using Docker for easy deployment and scalability. Update the `Dockerfile` as needed and build the Docker image:
```
docker build -t duckberry .
```

Run the Docker container:
```
docker run -p 8000:8000 duckberry
```

The application can be deployed to various platforms like Kubernetes, Azure App Services, or AWS App Runner for scalability and managed infrastructure.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
