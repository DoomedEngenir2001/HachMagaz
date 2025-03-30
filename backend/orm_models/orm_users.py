#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
#-------------------------------------------------------------#

class Users(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_users

    login        = Column(String(255),  index=True, unique=True, default=ORM_Base.str_None)
    hashPassword = Column(String(255),  index=True, default=ORM_Base.str_None)
    email        = Column(String(255),  index=True, default=ORM_Base.str_None)
    phone        = Column(String(255),  index=True, default=ORM_Base.str_None)
    createTime   = Column(String(255),  default=ORM_Base.str_None)
    lastSeen     = Column(String(255),  default=ORM_Base.str_None)
    

    #Связь с таблицей orders
    orders = relationship(ORM_Configuration.c_Orders,
                                 back_populates=ORM_Configuration.rel_user_to_orders)