#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String
#-------------------------------------------------------------#
from orm_configuration import ORM_Configuration
#-------------------------------------------------------------#

class ORM_Base:
    __tablename__ = ORM_Configuration.str_None
    id  = Column(Integer, primary_key=True, index=True)

    str_None        : str = ORM_Configuration.str_None
    str_Error       : str = ORM_Configuration.str_Error
    int_None        : int = ORM_Configuration.int_None
    int_Error       : int = ORM_Configuration.int_Error