# /quackberry/src/data/dataaccess.py
from typing import List, Dict
import duckdb
from src.api.schemas import ExampleSchema
from dotenv import load_dotenv
import os

load_dotenv()
DELTA_TABLE_PATHS = [os.getenv("DELTA_TABLE_PATHS")]

def read_delta(start: int, limit: int, filters: dict = None, table_index: int = 0) -> List[ExampleSchema]:
    delta_table_path = DELTA_TABLE_PATHS[table_index]
    query = f"""
    SELECT 
        *
    FROM delta_scan('{delta_table_path}')
    """
    if filters:
        conditions = []
        for field, value in filters.items():
            if isinstance(value, list):
                formatted_values = ", ".join(f"'{v}'" for v in value)
                conditions.append(f"{field} IN ({formatted_values})")
            else:
                conditions.append(f"{field} = '{value}'")
        query += f" WHERE {' AND '.join(conditions)}"
    
    query += f" LIMIT {limit} OFFSET {start}"
    
    return [ExampleSchema(**row) for row in duckdb.query(query).df().to_dict(orient='records')]