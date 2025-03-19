#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String
#-------------------------------------------------------------#
from db_creater import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
#-------------------------------------------------------------#

class Products(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_products

    name        = Column(String, index=True)
    description = Column(String, index=True)
    price       = Column(Integer, index=True)
    count       = Column(Integer, index=True)
    category    = Column(String, index=True)
    image       = Column(String, index=True)