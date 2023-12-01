import datetime
import logging

from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from models import models
from schemas import schemas

logger = logging.getLogger(__name__)


async def create_task(db: Session, task: schemas.STaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
    )
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    logger.info(f"Task created successfully: Title - {db_task.title}, Description - {db_task.description}")
    return db_task


async def get_task(db: Session, skip: int = 0, limit: int = 10):
    tasks = await db.execute(select(models.Task).offset(skip).limit(limit))
    tasks = tasks.scalars().all()
    return tasks


async def get_task_by_id(db: Session, task_id: int):
    query = select(models.Task).filter(models.Task.id == task_id)
    result = await db.execute(query)
    db_task = result.scalar()
    return db_task


async def update_task_by_id(db: Session, task_id: int, updated_task: schemas.STaskCreate):
    query = (
        update(models.Task)
        .where(models.Task.id == task_id)
        .values(title=updated_task.title, description=updated_task.description, created_at=datetime.datetime.now())
    )

    await db.execute(query)
    await db.commit()

    updated_task = await db.execute(select(models.Task).where(models.Task.id == task_id))
    updated_task = updated_task.scalar()
    logger.info(f"Task with ID {task_id} updated successfully: {updated_task.title} - {updated_task.description}")
    return updated_task


async def delete_task_by_id(db: Session, task_id: int):
    query = delete(models.Task).where(models.Task.id == task_id)
    await db.execute(query)
    await db.commit()
    logger.info(f"Task with ID {task_id} deleted successfully")
    return task_id
