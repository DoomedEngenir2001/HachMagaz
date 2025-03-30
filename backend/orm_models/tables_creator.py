import asyncio
from sqlalchemy.ext.asyncio import AsyncConnection
#-------------------------------------------------------------#
from session_handler import engine, Base
from orm_products import Products  # Импортируем модели, чтобы они были зарегистрированы
from orm_images import Images
from orm_productCards import ProductCards
#-------------------------------------------------------------#

async def initialize_tables(debug: bool = False) -> None:
    try:
        async with engine.begin() as connection:
            connection: AsyncConnection
            await connection.run_sync(Base.metadata.create_all)
        print("Модели успешно инициализированы.")
    except Exception as ex:
        if debug:
            print(f"Ошибка при инициализации моделей: {ex}")

if __name__ == "__main__":
    asyncio.run(initialize_tables())