import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from session_handler import AsyncSessionLocal
from orm_products import Products
from orm_productCards import ProductCards
from orm_images import Images



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

# await table.__table__.drop(bind=session.bind)
if __name__ == "__main__":
    # asyncio.run(insert_product_data())
    # asyncio.run(insert_images_data())
    asyncio.run(insert_productCards_data())

