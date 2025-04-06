#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orders_status import Order_status
from orm_base import ORM_Base
#-------------------------------------------------------------#

class Orders(ORM_Base, Order_status, Base ):
    __tablename__ = ORM_Configuration.t_orders

    user_id      = Column(Integer,      ForeignKey(f"{ORM_Configuration.t_users}.id"),
                           index=True, default=ORM_Base.int_None)
    email        = Column(String(255),  index=True, default=ORM_Base.str_None)
    phone        = Column(String(255),  index=True, default=ORM_Base.str_None)
    address      = Column(String(255),  index=True, default=ORM_Base.str_None)
    createTime   = Column(String(255),  default=ORM_Base.str_None)
    status       = Column(String(255),  default=ORM_Base.str_None)
    

    #Связь с таблицей users
    user = relationship(ORM_Configuration.c_Users,
                                 back_populates=ORM_Configuration.rel_orders_to_user)
    #Связь с таблицей transactions
    transactions = relationship(ORM_Configuration.c_Transactions,
                                 back_populates=ORM_Configuration.rel_orders_to_transactions)
    
    def __repr__(self):
        return f"Orders(id={self.id}, user_id={self.user_id}, email={self.email}, phone={self.phone}, address={self.address}, createTime={self.createTime}, status={self.status})"