import os, sys
def add_parent_folder_to_sys_path():
    """
    Добавляет родительскую папку текущего файла в sys.path.
    """
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Текущая директория файла
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))  # Родительская директория
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
        print(f"Родительская папка {parent_dir} добавлена в sys.path")
    else:
        print(f"Родительская папка {parent_dir} уже присутствует в sys.path")

# Вызов функции
add_parent_folder_to_sys_path()
from project_init import init
init()
#-------------------------------------------------------------#
import asyncio
from sqlalchemy.ext.asyncio             import AsyncConnection
#-------------------------------------------------------------#
from db_modules.session_handler         import engine, Base
#ORM models block №1
from orm_models.orm_products            import Products 
from orm_models.orm_images              import Images
from orm_models.orm_productCards        import ProductCards
#ORM models block №2
from orm_models.orm_users              import Users
from orm_models.orm_orders             import Orders
from orm_models.orm_transactions       import Transactions
#-------------------------------------------------------------#

async def initialize_tables(debug: bool = False) -> None:
    try:
        async with engine.begin() as connection:
            connection: AsyncConnection
            await connection.run_sync(Base.metadata.create_all)
        print("Модели успешно инициализированы.")
    except Exception as ex:
        if debug:
            print(f"Ошибка при инициализации таблиц: {ex}")

def create_tables(debug: bool = False) -> None:
    try:
        asyncio.run(initialize_tables(debug))
    except Exception as ex:
        if debug:
            print(f"Ошибка при создании таблиц: {ex}")

if __name__ == "__main__":
     create_tables(debug=True)