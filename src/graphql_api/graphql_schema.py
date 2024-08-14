# /quackberry/src/graphql_api/graphql_schema.py
import strawberry
from src.graphql_api.queries.example_query import ExampleQuery
from src.graphql_api.queries.example_sql_query import ExampleSQLQuery

@strawberry.type
class Query(
    ExampleQuery,
    ExampleSQLQuery
):
    pass

schema = strawberry.Schema(query=Query)