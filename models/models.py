import datetime

from sqlalchemy import Integer, String, text
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


# from DATABASE_URL import Base, sync_engine


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("(DATETIME('now'))"))


# Base.metadata.create_all(bind=sync_engine)
