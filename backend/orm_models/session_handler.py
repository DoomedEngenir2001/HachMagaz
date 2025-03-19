from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db_creater import AsyncSessionLocal

async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
