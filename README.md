# fastapi_porject
Fastapi Project

This is a FastAPI app that sums numbers in sublists using multiprocessing.

Prerequisites

- Python 3.7 or above
- FastAPI
- Uvicorn
- requests

To run App command
    "python main.py"
To run test cases
    "python test_endpoint.py"

To access url
    go to http://127.0.0.1:8000/docs

For add list of number input example-

    {
      "batchid": "id1",
      "payload": [[1, 2], [3, 4]]
    }

Response example -
    {
  "batchid": "id1",
  "response": [ 3, 7],
  "status": "completed",
  "start_time": "31/05/2024, 11:38:16",
  "end_time": "31/05/2024, 11:38:18"
}
