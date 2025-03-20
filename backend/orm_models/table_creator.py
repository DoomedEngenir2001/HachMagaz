import asyncio
from db_creater import engine, Base
from orm_products import Products  # Импортируем модели, чтобы они были зарегистрированы

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_models())