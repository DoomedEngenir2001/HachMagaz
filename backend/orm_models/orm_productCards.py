#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
#-------------------------------------------------------------#
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from db_modules.session_handler import get_session, AsyncSessionLocal
from sqlalchemy import update
class ProductCards(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_productsCards

    product_id  = Column(Integer,     ForeignKey(f"{ORM_Configuration.t_products}.id"),
                            index=True, nullable=False)
    image_id    = Column(Integer,     ForeignKey(f"{ORM_Configuration.t_images}.id"),
                            index=True, nullable=False)
    title       = Column(String(255), index=True, default=ORM_Base.str_None)
    description = Column(String(255), index=True, default=ORM_Base.str_None)
    specPrice   = Column(Integer,     index=True, default=ORM_Base.int_None)
    limit       = Column(Integer,     index=True, default=ORM_Base.int_None)

    #Cвязь с таблицей product
    product = relationship(ORM_Configuration.c_Products,
                             back_populates=ORM_Configuration.rel_productsCards_to_product)
    #Cвязь с таблицей image
    image = relationship(ORM_Configuration.c_Images,
                           back_populates=ORM_Configuration.rel_productsCard_to_image)
    #Cвязь с таблицей transactions
    transactions = relationship(ORM_Configuration.c_Transactions,
                                  back_populates=ORM_Configuration.rel_productsCards_to_transactions)
    
    @staticmethod
    async def update_product_card(id_: int, image_: int, title_: str, desc_: str, 
                                  price_: int, limit_: int):
        async with  AsyncSessionLocal() as session:
            session: AsyncSession
            stmt = update(ProductCards).where(ProductCards.product_id == id_).values(
                # ProductCards.id: id,
                # ProductCards.image_id: image,
                title=title_,
                description=desc_,
                specPrice=price_,
                limit=limit_
            )
            result = await session.execute(stmt)
            await session.commit()
    def __repr__(self):
        return f"ProductCards(id={self.id}, product_id={self.product_id}, image_id={self.image_id}, title={self.title}, description={self.description}, specPrice={self.specPrice}, limit={self.limit})"