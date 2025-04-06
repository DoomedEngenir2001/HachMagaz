#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.future import select
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
#-------------------------------------------------------------#
from side_methods import get_current_datetime
from hash_methods import verify_password
#-------------------------------------------------------------#
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from db_modules.session_handler import get_session, AsyncSessionLocal
#-------------------------------------------------------------#

class Users(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_users

    login        = Column(String(255),  index=True, unique=True, default=ORM_Base.str_None)
    hashPassword = Column(String(255),  index=True, unique=True, default=ORM_Base.str_None)
    email        = Column(String(255),  index=True, unique=True, default=ORM_Base.str_None)
    phone        = Column(String(255),  index=True, unique=True, default=ORM_Base.str_None)
    createTime   = Column(String(255),  default=ORM_Base.str_None)
    lastSeen     = Column(String(255),  default=ORM_Base.str_None)
    

    #Связь с таблицей orders
    orders = relationship(ORM_Configuration.c_Orders,
                                 back_populates=ORM_Configuration.rel_user_to_orders)
    
    def __repr__(self):
        return f"Users(id={self.id}, login={self.login}, hashPassword={self.hashPassword}, email={self.email}, phone={self.phone}, createTime={self.createTime}, lastSeen={self.lastSeen})"

    @staticmethod
    async def is_login_exist(login: str) -> bool:
        """
        Проверяет, существует ли запись с указанным email в базе данных.
        """
        async with AsyncSessionLocal() as session:
           session : AsyncSession
           stmt = select(Users).where(Users.login == login)
           result = await session.execute(stmt)
           user = result.scalar_one_or_none()
           return user is not None

    @staticmethod
    async def is_email_exist(email: str) -> bool:
        async with AsyncSessionLocal() as session:
           session : AsyncSession
           stmt = select(Users).where(Users.email == email)
           result = await session.execute(stmt)
           user = result.scalar_one_or_none()
           return user is not None
    
    @staticmethod
    async def is_phone_exist(phone: str) -> bool:
        async with AsyncSessionLocal() as session:
           session : AsyncSession
           stmt = select(Users).where(Users.phone == phone)
           result = await session.execute(stmt)
           user = result.scalar_one_or_none()
           return user is not None
        
    async def update_last_seen(self) -> None:
        async with AsyncSessionLocal() as session:
            session: AsyncSession
            self.lastSeen = get_current_datetime()
            await session.refresh(self)  # Обновляем объект из базы данных

    async def verify_password(self, inputPassword) -> bool:
        async with AsyncSessionLocal() as session:
            session: AsyncSession
            return await verify_password(inputPassword, self.hashPassword)
    
    @staticmethod
    async def get_rowByLogin( login: str) -> ORM_Base:
        async with AsyncSessionLocal() as session:
            session: AsyncSession
            stmt = select(Users).where(Users.login == login)
            result = await session.execute(stmt)
            user = result.scalar_one_or_none()
            return user if isinstance(user, Users) else ORM_Base.str_Error

    @staticmethod
    async def get_rowByEmail( email: str) -> ORM_Base:
        async with AsyncSessionLocal() as session:
            session: AsyncSession
            stmt = select(Users).where(Users.email == email)
            result = await session.execute(stmt)
            user = result.scalar_one_or_none()
            return user if isinstance(user, Users) else ORM_Base.str_Error
    
    @staticmethod
    async def get_rowByPhone( phone: str) -> ORM_Base:
        async with AsyncSessionLocal() as session:
            session: AsyncSession
            stmt = select(Users).where(Users.phone == phone)
            result = await session.execute(stmt)
            user = result.scalar_one_or_none()
            return user if isinstance(user, Users) else ORM_Base.str_Error
