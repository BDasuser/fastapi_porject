from pydantic import BaseModel
from typing import List

class Payload(BaseModel):
    batchid: str
    payload: List[List[int]]

class Output(BaseModel):
    batchid: str
    response: List[int]
    status: str
    start_time: str
    end_time: str