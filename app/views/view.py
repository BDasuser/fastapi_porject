import multiprocessing
from datetime import datetime
import logging

logging.basicConfig(filename='application.log', filemode="a", format='%(asctime)s %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def add_num(payload):
    return sum(payload)

def process_item(item: dict):
    batchid = item.batchid
    payload = item.payload

    start_time = datetime.now()
    logger.info(f"started {batchid} at {start_time}")

    
    with multiprocessing.Pool() as pool:
        result = pool.map(add_num, payload)

    end_time = datetime.now()
    logger.info(f"Completed {batchid} at {end_time}")

    response = {
        "batchid": batchid,
        "response": result,
        "status": "completed",
        "start_time": start_time.strftime("%d/%m/%Y, %H:%M:%S"),
        "end_time": end_time.strftime("%d/%m/%Y, %H:%M:%S")
    }

    logger.info(f"Response is {response}")
    return response
