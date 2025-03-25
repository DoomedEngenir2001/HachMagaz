#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from session_handler import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
#-------------------------------------------------------------#

class Products(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_products

    title        = Column(String(255),  index=True, default=ORM_Base.str_None)
    description  = Column(String(255),  index=True, default=ORM_Base.str_None)
    price        = Column(Integer,      index=True, default=ORM_Base.int_None)
    countInStock = Column(Integer,      index=True, default=ORM_Base.int_None)
    

    #Связь с таблицей productCards
    productCards = relationship(ORM_Configuration.c_ProductCards,
                                 back_populates=ORM_Configuration.rel_product_to_productsCards)