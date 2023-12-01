from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from schemas.schemas import STask, STaskCreate, STaskList
from crud import crud
from database import get_db

router = APIRouter()


@router.post("/", response_model=STask)
async def create_task(task: STaskCreate, db: Session = Depends(get_db)):
    db_task = await crud.create_task(db=db, task=task)
    return db_task


@router.get("/", response_model=STaskList)
async def get_all_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tasks = await crud.get_task(db=db, skip=skip, limit=limit)
    return {"tasks": tasks}
    # return STaskList(tasks=tasks)


@router.get("/{task_id}", response_model=STask)
async def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    db_task = await crud.get_task_by_id(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return db_task


@router.put("/{task_id}", response_model=STask)
async def update_task(task_id: int, updated_data: STaskCreate, db: Session = Depends(get_db)):
    updated_task = await crud.update_task_by_id(db=db, task_id=task_id, updated_task=updated_data)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return updated_task


@router.delete("/{task_id}", response_model=str)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = await crud.get_task_by_id(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")

    deleted_task_id = await crud.delete_task_by_id(db=db, task_id=task_id)

    return f"Задача с id {deleted_task_id} удалена"
