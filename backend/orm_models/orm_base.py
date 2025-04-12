#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.sql import text  # Импортируем функцию text
#-------------------------------------------------------------#
from orm_configuration import ORM_Configuration
from db_modules.session_handler import get_session, AsyncSessionLocal
#-------------------------------------------------------------#

class ORM_Base:
    __tablename__ = ORM_Configuration.str_None
    id  = Column(Integer, primary_key=True, index=True)

    str_None        : str = ORM_Configuration.str_None
    str_Error       : str = ORM_Configuration.str_Error
    int_None        : int = ORM_Configuration.int_None
    int_Error       : int = ORM_Configuration.int_Error

    async def get_rowById(cls, id : int):
        async with AsyncSessionLocal() as session:
            session : AsyncSession
            stmt = select(cls).where(cls.id == id)
            result = await session.execute(stmt)
            return result.scalar()

    #---------------------Create, Update, Delete-----------------#

    async def add_row(self) -> bool:
        try:
            async with AsyncSessionLocal() as session:
                session : AsyncSession
                session.add(self)
                await session.commit()
                await session.refresh(self)
            return True
        except Exception as ex:
            raise ex
            return False
    
    async def update_row(self):
        async with AsyncSessionLocal() as session:
            session : AsyncSession
            await session.commit()
            await session.refresh(self)

    async def set_values(self):
        async with AsyncSessionLocal() as session:
            session : AsyncSession
            await session.commit()

    async def delete_row(self):
        async with AsyncSessionLocal() as session:
            session : AsyncSession
            session.delete(self)
            await session.commit()
    
    #-------------------------------------------------------------#

    async def toDict(self) -> dict:
        """
        Преобразует объект в словарь.
        """
        return {
            "id": self.id,
            **{column.name: getattr(self, column.name) for column in self.__table__.columns}
        }

    @classmethod
    async def get_table_data(cls):
        async with AsyncSessionLocal() as session:
            session : AsyncSession
            stmt = select(cls)
            result = await session.execute(stmt)
            return result.scalars().all()
    
    @classmethod
    async def drop_table_data(cls):
        async with AsyncSessionLocal() as session:
            session : AsyncSession
            stmt = text(f"DELETE FROM {cls.__tablename__};")
            await session.execute(stmt)
            await session.commit()
            print(f"Данные таблицы {cls.__tablename__} успешно удалены.")

    @classmethod
    async def drop_table(cls):
        """Асинхронное удаление таблицы из базы данных"""
        async with AsyncSessionLocal() as session:
            session : AsyncSession
            try:
                 # Отключаем проверки внешних ключей
                await session.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))

                await session.execute(  text(f"DROP TABLE IF EXISTS {cls.__tablename__} CASCADE;")  )
                await session.commit()
                print(f"Таблица {cls.__tablename__} успешно удалена.")
                
            except Exception as ex:
                print(f"Ошибка при удалении таблицы {cls.__tablename__}: \n{ex}")
            finally:
            # Включаем проверки внешних ключей обратно
                await session.execute(text("SET FOREIGN_KEY_CHECKS = 1;"))

        return cls.__tablename__
   