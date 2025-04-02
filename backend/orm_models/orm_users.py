#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
from side_methods import get_current_datetime
#-------------------------------------------------------------#
from hash_methods import hash_password, verify_password
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
    
    def __init__( self, 
                  login      : str,
                  password   : str,
                  email      : str = ORM_Base.str_None, 
                  phone      : str = ORM_Base.str_None, 
                  createTime : str = get_current_datetime(), 
                  lastSeen   : str = get_current_datetime()):
        
        self.login        = login
        self.hashPassword = hash_password(password)
        self.email        = email
        self.phone        = phone
        self.createTime   = createTime
        self.lastSeen     = lastSeen
        self.add_row()

    def login_user(self, password: str) -> bool:
        """
        Проверяет правильность пароля пользователя.
        """
        return verify_password(self.hashPassword, password)

   