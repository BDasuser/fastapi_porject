import multiprocessing
from datetime import datetime
from src.log.logging import applog


def add_num(payload):
    return sum(payload)

def process_item(item: dict):
    batchid = item.batchid
    payload = item.payload

    start_time = datetime.now()
    applog.info(f"started {batchid} at {start_time}")

    
    with multiprocessing.Pool() as pool:
        result = pool.map(add_num, payload)

    end_time = datetime.now()
    applog.info(f"Completed {batchid} at {end_time}")

    response = {
        "batchid": batchid,
        "response": result,
        "status": "completed",
        "start_time": start_time.strftime("%d/%m/%Y, %H:%M:%S"),
        "end_time": end_time.strftime("%d/%m/%Y, %H:%M:%S")
    }

    applog.info(f"Response is {response}")
    return response
