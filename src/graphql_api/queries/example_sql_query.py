# /quackberry/src/graphql_api/queries/example_sql_query.py
import strawberry
from typing import List, Optional
import duckdb
from src.data.dataaccess import DELTA_TABLE_PATHS
from src.graphql_api.types.example_sql_type import ExampleSQLType

@strawberry.type
class ExampleSQLQuery:
    @strawberry.field
    def example_sql_query(self, filters: Optional[str] = None, table_index: int = 0) -> List[ExampleSQLType]:
        filter_dict = {}
        if filters:
            filter_pairs = filters.split(',')
            for pair in filter_pairs:
                field, value = pair.split('=')
                filter_dict[field] = value
        
        delta_table_path = DELTA_TABLE_PATHS[table_index]
        query = f"""
        SELECT 
            *,
            COUNT(field1) as count_field1
        FROM 
            delta_scan('{delta_table_path}')
        """
        if filter_dict:
            conditions = []
            for field, value in filter_dict.items():
                conditions.append(f"{field} = '{value}'")
            query += f" WHERE {' AND '.join(conditions)}"
        
        query += """
        GROUP BY
            field1, field2
        ORDER BY
            count_field1 DESC;
        """
        return [ExampleSQLType(**row) for row in duckdb.query(query).df().to_dict(orient='records')]