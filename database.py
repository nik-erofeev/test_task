from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import DB_NAME

# DATABASE_URL = f"sqlite:///{DB_NAME}" # sync

DATABASE_URL = f"sqlite+aiosqlite:///{DB_NAME}"


sync_engine = create_engine(
    url=DATABASE_URL,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)


async_engine = create_async_engine(
    url=DATABASE_URL,
    echo=False,
)


session_factory = sessionmaker(
    bind=sync_engine,
    autoflush=False,
    expire_on_commit=False,
)

async_session_factory = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


# def get_db():
#     with session_factory() as session:
#         yield session_factory


async def get_db():
    async with async_session_factory() as session:
        yield session
