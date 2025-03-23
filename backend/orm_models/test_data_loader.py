import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from db_creater import AsyncSessionLocal
from orm_products import Products
from orm_productCards import ProductCards
from orm_images import Images



async def insert_test_data():
    async with AsyncSessionLocal() as session:
        session : AsyncSession
        test_products = [
            Products(title="Ноутбук", description="Игровой ноутбук", price=1200, countInStock=5),
            Products(title="Смартфон", description="Флагманский смартфон", price=900, countInStock=10),
            Products(title="Наушники", description="Беспроводные наушники", price=150, countInStock=20),
            Products(title="Монитор", description="4K монитор", price=500, countInStock=7),
        ]

        session.add_all(test_products)
        await session.commit()
        print("Тестовые данные добавлены!")

if __name__ == "__main__":
    asyncio.run(insert_test_data())
