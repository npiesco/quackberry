# /quackberry/src/api/schemas.pysrc/api/schemas.py
from pydantic import BaseModel
from typing import Optional

class ExampleSchema(BaseModel):
    field1: Optional[str] = None
    field2: Optional[int] = None