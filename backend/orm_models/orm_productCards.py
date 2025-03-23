#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from db_creater import Base
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

    # #Cвязь с таблицей product
    # product = relationship(ORM_Configuration.t_products,
    #                          back_populates=ORM_Configuration.rel_productsCards_to_product)
    # #Cвязь с таблицей image
    # image = relationship(ORM_Configuration.t_images,
    #                        back_populates=ORM_Configuration.rel_productsCard_to_image)