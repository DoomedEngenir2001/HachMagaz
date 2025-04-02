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
from sqlalchemy.ext.asyncio import AsyncSession
from db_modules.session_handler import AsyncSessionLocal
#-------------------------------------------------------------#
#ORM models block №1
from orm_models.orm_products            import Products 
from orm_models.orm_images              import Images
from orm_models.orm_productCards        import ProductCards
#ORM models block №2
from orm_models.orm_users              import Users
from orm_models.orm_orders             import Orders
from orm_models.orm_transactions       import Transactions
#-------------------------------------------------------------#
from logic.l_users import create_user
#-------------------------------------------------------------#

async def insert_product_data():
    async with AsyncSessionLocal() as session:
        session : AsyncSession
        test_products = [
            Products(title="Пицца",                 description="Вкусная пицца",   price=120, countInStock=10),
            Products(title="Пиво",                  description="Балтика №8",      price=78,  countInStock=10),
            Products(title="Энергетик",             description="Ягуар б/а синий", price=76,  countInStock=21),
            Products(title="Медовик",               description="Кусок 200 г.",    price=110, countInStock=7),
            Products(title="Вода",                  description="Шишкин лес 8 л.", price=115, countInStock=6),
            Products(title="Сосиска в тесте",       description="Мясо - курица",   price=58,  countInStock=5),
            Products(title="Самса",                 description="Самса с сыром",   price=68,  countInStock=4),
            Products(title="Трубочка со сгущенкой", description="100 грамм",       price=54,  countInStock=3),
        ]

        session.add_all(test_products)
        await session.commit()
        print("Тестовые продукты добавлены!")

async def insert_images_data():
    async with AsyncSessionLocal() as session:
        session : AsyncSession
        test_images = [
            Images(file_path="backend\images\Балтика.webp"),
            Images(file_path="backend\images\Вода.jpg"),
            Images(file_path="backend\images\Медовик.jpg"),
            Images(file_path="backend\images\Пиццуля.PNG"),
            Images(file_path="backend\images\Самса.webp"),
            Images(file_path="backend\images\Сосиска в тесте.jpg"),
            Images(file_path="backend\images\Трубочка.jpg"),
            Images(file_path="backend\images\Шаурма.jpg"),
            Images(file_path="backend\images\Яга.webp"),
        ]

        session.add_all(test_images)
        await session.commit()
        print("Тестовые картинки добавлены!")

async def insert_productCards_data():
    async with AsyncSessionLocal() as session:
        session : AsyncSession
        test_images = [
            ProductCards(product_id=1, image_id=4, title="Пицца",                 description="Вкусная пицца",   specPrice=120, limit=10),
            ProductCards(product_id=2, image_id=9, title="Пиво",                  description="Балтика №8",      specPrice=78,  limit=10),
            ProductCards(product_id=3, image_id=8, title="Энергетик",             description="Ягуар б/а синий", specPrice=76,  limit=21),
            ProductCards(product_id=4, image_id=3, title="Медовик",               description="Кусок 200 г.",    specPrice=110, limit=7),
            ProductCards(product_id=5, image_id=2, title="Вода",                  description="Шишкин лес 8 л.", specPrice=115, limit=6),
            ProductCards(product_id=6, image_id=6, title="Сосиска в тесте",       description="Мясо - курица",   specPrice=58,  limit=5),
            ProductCards(product_id=7, image_id=5, title="Самса",                 description="Самса с сыром",   specPrice=68,  limit=4),
            ProductCards(product_id=8, image_id=7, title="Трубочка со сгущенкой", description="100 грамм",       specPrice=54,  limit=3),
        ]

        session.add_all(test_images)
        await session.commit()
        print("Тестовые карточки товара добавлены!")

async def insert_users_data():
    obj_a = await create_user(login="admin", password="12345", email="noemail@gmail.com", phone="8918808733")
    obj_b = await create_user(login="bot", password="12345", email="fakeemail@gmail.com", phone="8888888881")

    print("Тестовые пользователи добавлены!")
    print(obj_a, obj_b)

# await table.__table__.drop(bind=session.bind)
if __name__ == "__main__":
    # try:
    #     asyncio.run(insert_product_data())
    # except Exception as ex:
    #     print(f"Ошибка при добавлении тестовых продуктов: {ex}")

    # try:
    #     asyncio.run(insert_images_data())
    # except Exception as ex:
    #     print(f"Ошибка при добавлении тестовых изображений: {ex}")

    # try:
    #     asyncio.run(insert_productCards_data())
    # except Exception as ex:
    #     print(f"Ошибка при добавлении тестовых карточек товара: {ex}")

    try:
        asyncio.run(insert_users_data())
    except Exception as ex:
        print(f"Ошибка при добавлении тестовых пользователей: {ex}")

