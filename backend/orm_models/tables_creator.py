import asyncio
from sqlalchemy.ext.asyncio import AsyncConnection
#-------------------------------------------------------------#
from db_creater import engine, Base
from orm_products import Products  # Импортируем модели, чтобы они были зарегистрированы
from orm_images import Images
from orm_productCards import ProductCards
#-------------------------------------------------------------#

async def init_models():
    try:
        async with engine.begin() as connection:
            connection : AsyncConnection
            await connection.run_sync(Base.metadata.create_all)
    finally:
        await connection.close()

if __name__ == "__main__":
    asyncio.run(init_models())