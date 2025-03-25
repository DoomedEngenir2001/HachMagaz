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
        print("Тестовые данные добавлены!")

# await table.__table__.drop(bind=session.bind)
if __name__ == "__main__":
    asyncio.run(insert_product_data())

