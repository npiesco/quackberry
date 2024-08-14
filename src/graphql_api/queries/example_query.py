# /quackberry/src/graphql_api/queries/example_query.py
import strawberry
from typing import List

from src.graphql_api.types.example_type import ExampleType
from src.data.dataaccess import read_delta

@strawberry.type
class ExampleQuery:
    @strawberry.field
    def example_query(self, start: int = 0, limit: int = 100, filters: str = None) -> List[ExampleType]:
        filter_dict = {}
        if filters:
            filter_pairs = filters.split(',')
            for pair in filter_pairs:
                field, value = pair.split('=')
                filter_dict[field] = value
        data = read_delta(start, limit, filter_dict)
        return [ExampleType(**row) for row in data]