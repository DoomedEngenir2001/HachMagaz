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

class Images(ORM_Base, Base):
    __tablename__ = ORM_Configuration.t_images

    file_path   = Column(String(255), index=True, default=ORM_Base.str_None)
    UID         = Column(String(255), index=True, default=ORM_Base.str_None)
    hash        = Column(String(255), index=True, default=ORM_Base.str_None)

    #Cвязь с таблицей productCard
    productCards = relationship(ORM_Configuration.c_ProductCards,
                                 back_populates=ORM_Configuration.rel_image_to_productsCard)
    
    @staticmethod
    def generate_random_UID(length: int = 4):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def __init__(self, file_path : str, UID : str = generate_random_UID()):
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as file:
                # Читаем файл блоками для обработки больших файлов
                for chunk in iter(lambda: file.read(4096), b""):
                    hash_sha256.update(chunk)
            self.hash = hash_sha256.hexdigest()
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
        except Exception as e:
            print(f"Ошибка при вычислении хэша: {e}")
            
        self.file_path = file_path
        self.UID = UID
        self.add_row()
    