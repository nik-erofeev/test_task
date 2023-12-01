import datetime

from pydantic import BaseModel


class STaskCreate(BaseModel):
    title: str
    description: str


class STask(STaskCreate):
    id: int
    created_at: datetime.datetime

    # class Config:
    #     from_attributes = True


class STaskList(BaseModel):
    tasks: list[STask] = []

    # class Config:
    #     from_attributes = True
