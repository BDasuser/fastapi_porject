from fastapi import APIRouter, HTTPException

from src.log.logging import applog
from src.view import views
from src.validation.validate import Payload, Output

router = APIRouter()

@router.get("/home")
def index():
    return {"message":"App is Running"}

@router.post("/add", response_model=Output)
def add(payload: Payload):
    applog.info("Addition of numbers started")
    try:
        response = views.process_item(payload)
        return response
    except Exception as ex:
        applog.error(f"Error occured due to {ex}")
        raise HTTPException(status_code=500, detail=str(ex))
