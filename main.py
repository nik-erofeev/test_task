import logging

from fastapi import FastAPI

from routers.task import router as task_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="app.log",
    filemode="a",
)

app = FastAPI()

app.include_router(router=task_router, prefix="/task", tags=["tasks"])



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8006)
