#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orders_status import Order_status
from orm_base import ORM_Base
#-------------------------------------------------------------#

class Transactions(ORM_Base, Order_status, Base ):
    __tablename__ = ORM_Configuration.t_transactions

    order_id       = Column(Integer,      ForeignKey(f"{ORM_Configuration.t_orders}.id"),
                           index=True, default=ORM_Base.int_None)
    productCard_id = Column(Integer,      ForeignKey(f"{ORM_Configuration.t_productsCards}.id"),
                           index=True, default=ORM_Base.int_None)
    count          = Column(Integer,      index=True, default=ORM_Base.int_None)
    price          = Column(Integer,      index=True, default=ORM_Base.int_None)
    createTime     = Column(String(255),  default=ORM_Base.str_None)
    bankCardInfo   = Column(String(255),  default=ORM_Base.str_None)

    #Связь с таблицей orders
    order = relationship(ORM_Configuration.c_Orders,
                                 back_populates=ORM_Configuration.rel_transactions_to_orders)
    #Связь с таблицей productsCards
    productCard = relationship(ORM_Configuration.c_ProductCards,
                                 back_populates=ORM_Configuration.rel_transactions_to_productsCards)
    
    def toDict(self)-> dict:
        return {
            "class" : self.__class__.__name__,
            "id": self.id,
            "order_id": self.order_id,
            "productCard_id": self.productCard_id,
            "count": self.count,
            "price": self.price,
            "createTime": self.createTime,
            "bankCardInfo": self.bankCardInfo,
        }