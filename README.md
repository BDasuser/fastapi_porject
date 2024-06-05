# fastapi_porject
Fastapi Project

This is a FastAPI app that sums numbers in sublists using multiprocessing.

Files Overview

- main.py: Entry point of the FastAPI application.
- app/controller.py: Defines the API endpoints and handles incoming requests.
- app/model.py: Contains the data models for request and response using Pydantic.
- app/view.py: Contains the logic.
- tests/test.py: Contains unit tests for the addition functionality.

Prerequisites

- Python 3.7 or above
- FastAPI
- Uvicorn
- requests

To run App command
    "python main.py"
To run test cases
    "python test.py"

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
