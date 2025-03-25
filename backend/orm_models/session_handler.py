#-------------------------------------------------------------#
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker, AsyncEngine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from typing import AsyncGenerator
#-------------------------------------------------------------#
from database_configuration import DatabaseConfiguration
#-------------------------------------------------------------#

DATABASE_URL : str = DatabaseConfiguration.DATABASE_URL

engine : AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal : async_sessionmaker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Базовый класс для декларативных моделей
Base : DeclarativeMeta = declarative_base()

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Асинхронная генераторная функция для предоставления сессии базы данных.

    Эта функция создает экземпляр `AsyncSession` с использованием контекстного менеджера
    `AsyncSessionLocal`. Она возвращает объект сессии для выполнения операций с базой данных
    и обеспечивает корректное освобождение ресурсов после использования сессии.

    Возвращает:
        AsyncSession: Экземпляр асинхронной сессии базы данных.
    """
    async with AsyncSessionLocal() as session:
        session : AsyncSession
        yield session