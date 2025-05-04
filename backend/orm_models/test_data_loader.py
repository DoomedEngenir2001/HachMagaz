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
from logic.l_products import create_product_row
from logic.l_users import create_user_row
from logic.l_images import create_image_row
from logic.l_productCards import create_productCard_row
from tables_creator import initialize_tables
#-------------------------------------------------------------#

async def insert_products_data() -> list[Products]:
    productslist = [
        await create_product_row(title="Пицца",                 description="Вкусная пицца",   price=120, countInStock=10),
        await create_product_row(title="Пиво",                  description="Балтика №8",      price=78,  countInStock=10),
        await create_product_row(title="Энергетик",             description="Ягуар б/а синий", price=76,  countInStock=21),
        await create_product_row(title="Медовик",               description="Кусок 200 г.",    price=110, countInStock=7),
        await create_product_row(title="Вода",                  description="Шишкин лес 8 л.", price=115, countInStock=6),
        await create_product_row(title="Сосиска в тесте",       description="Мясо - курица",   price=58,  countInStock=5),
        await create_product_row(title="Самса",                 description="Самса с сыром",   price=68,  countInStock=4),
        await create_product_row(title="Трубочка со сгущенкой", description="100 грамм",       price=54,  countInStock=3),
        await create_product_row(title="Шаурма",                description="Курица с овощами",price=150, countInStock=2),
    ]

    print("Тестовые продукты добавлены!")
    print(productslist)
    return productslist

async def insert_images_data() -> list[Images]:
    imagesList = [
        await create_image_row(file_path="images/Пиццуля.PNG"),
        await create_image_row(file_path="images/Балтика.webp"),
        await create_image_row(file_path="images/Яга.webp"),
        await create_image_row(file_path="images/Медовик.jpg"),
        await create_image_row(file_path="images/Вода.jpg"),
        await create_image_row(file_path="images/Сосиска в тесте.jpg"),
        await create_image_row(file_path="images/Самса.webp"),
        await create_image_row(file_path="images/Трубочка.jpg"),
        await create_image_row(file_path="images/Шаурма.jpg"),
    ]
    
    print("Тестовые картинки добавлены!")
    print(imagesList)
    return imagesList

async def insert_productCards_data(productslist : list[Products], imagesList : list[Images]) -> list[ProductCards]:
    productCardsList = []
    for i in range( len(productslist) ):
            productCard = await create_productCard_row(
                                                        product_id  = productslist[i].id,
                                                        image_id    = imagesList[i].id,
                                                        title       = productslist[i].title,
                                                        description = productslist[i].description, 
                                                        specPrice   = productslist[i].price, 
                                                        limit       = productslist[i].countInStock
                                                        )
            productCardsList.append(productCard)

    print("Тестовые карточки товара добавлены!")
    print(productCardsList)
    return productCardsList

async def insert_users_data() -> list[Users]:
    obj_a = await create_user_row(login="admin", password="12345", email="noemail@gmail.com", phone="8918808733")
    obj_b = await create_user_row(login="bot", password="12345", email="fakeemail@gmail.com", phone="8888888881")

    print("Тестовые пользователи добавлены!")
    print(obj_a, obj_b)
    return [obj_a, obj_b]

async def init_db():
   # loop = asyncio.get_event_loop()
    await initialize_tables(debug=True)
    productslist = await insert_products_data()
    imagesList = await insert_images_data()
    await insert_productCards_data(productslist, imagesList)
    await insert_users_data()
    print('БАЗА ДАННЫХ ЕБАTЬ ГОТОВА!!!!!!!')
   # loop.close()
# await table.__table__.drop(bind=session.bind)
if __name__ == "__main__":
    # try:
    #     asyncio.run(insert_products_data())
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

