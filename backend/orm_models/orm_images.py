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
from sqlalchemy.ext.asyncio import AsyncSession
from db_modules.session_handler import get_session, AsyncSessionLocal
from sqlalchemy.future import select
#-------------------------------------------------------------#

class Images(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_images

    file_path   = Column(String(255), index=True,  default=ORM_Base.str_None)
    UID         = Column(String(255), unique=True, index=True, default=ORM_Base.str_None)
    hash        = Column(String(255), index=True,  default=ORM_Base.str_None)

    #Cвязь с таблицей productCard
    productCards = relationship(ORM_Configuration.c_ProductCards,
                                 back_populates=ORM_Configuration.rel_image_to_productsCard)
    @staticmethod
    async def get_image_id_by_path(path:str)->int:
        async with AsyncSessionLocal() as session:
            session: AsyncSession
            stmt = select(Images).where(Images.file_path == path)
            result = await session.execute(stmt)
            print(result)
            image = result.scalar_one_or_none()
            if isinstance(image, Images):
                return image.UID
            else:
                ORM_Base.str_Error 

    def __repr__(self):
        return f"Images(id={self.id}, file_path={self.file_path}, UID={self.UID}, hash={self.hash})"
    