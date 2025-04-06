#-------------------------------------------------------------#
from sqlalchemy import Column, Integer, String, ForeignKey
import hashlib
from sqlalchemy.orm import relationship
#-------------------------------------------------------------#
import random, string
#-------------------------------------------------------------#
from db_modules.session_handler import Base
from orm_configuration import ORM_Configuration
from orm_base import ORM_Base
#-------------------------------------------------------------#
from hash_methods import get_fileHash
from side_methods import generate_random_UID
#-------------------------------------------------------------#

class Images(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_images

    file_path   = Column(String(255), index=True,  default=ORM_Base.str_None)
    UID         = Column(String(255), unique=True, index=True, default=ORM_Base.str_None)
    hash        = Column(String(255), index=True,  default=ORM_Base.str_None)

    #Cвязь с таблицей productCard
    productCards = relationship(ORM_Configuration.c_ProductCards,
                                 back_populates=ORM_Configuration.rel_image_to_productsCard)
    

    