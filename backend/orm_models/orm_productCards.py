#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
#-------------------------------------------------------------#

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
    
    def __init__(self, product_id : int, image_id : int, title : str, description : str, specPrice : int, limit : int):
        self.product_id = product_id
        self.image_id = image_id
        self.title = title
        self.description = description
        self.specPrice = specPrice
        self.limit = limit
        self.add_row()