# /quackberry/src/graphql_api/types/example_sql_type.py
import strawberry

@strawberry.type
class ExampleSQLType:
    field1: str
    field2: int
    count_field1: int