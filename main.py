from fastapi import FastAPI
import uvicorn

from app.controller import router


app = FastAPI(title="App")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app")