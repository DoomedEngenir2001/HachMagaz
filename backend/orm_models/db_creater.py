#-------------------------------------------------------------#
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
#-------------------------------------------------------------#
from database_configuration import DatabaseConfiguration
#-------------------------------------------------------------#

DATABASE_URL : str = DatabaseConfiguration.DATABASE_URL

engine : AsyncSession = create_async_engine(DATABASE_URL, echo=True)


AsyncSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Базовый класс для декларативных моделей
Base = declarative_base()