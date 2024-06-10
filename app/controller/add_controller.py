from fastapi import APIRouter, HTTPException
import logging

from views import view
from models.model import Payload, Output


logging.basicConfig(filename='application.log', filemode="a", format='%(asctime)s %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/home")
def index():
    return {"message":"App is Running"}

@router.post("/add", response_model=Output)
def add(payload: Payload):
    logger.info("Addition of numbers started")
    try:
        response = view.process_item(payload)
        return response
    except Exception as ex:
        logger.error(f"Error occured due to {ex}")
        raise HTTPException(status_code=500, detail=str(ex))
