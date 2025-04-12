#-------------------------------------------------------------#
from typing import Union
#-------------------------------------------------------------#
from orm_models.orm_images    import Images
from orm_models.orm_base      import ORM_Base
#-------------------------------------------------------------#
from l_errors                 import NoSuchFileError
#-------------------------------------------------------------#
from side_methods             import check_file_exists, generate_random_UID
#-------------------------------------------------------------#
from hash_methods             import get_fileHash
#-------------------------------------------------------------#

# file_path   = Column(String(255), index=True,  default=ORM_Base.str_None)
#     UID         = Column(String(255), unique=True, index=True, default=ORM_Base.str_None)
#     hash        = Column(String(255), index=True,  default=ORM_Base.str_None)


    # def __init__(self, file_path : str):
    #     self.hash = get_fileHash(file_path)
    #     self.file_path = file_path
    #     self.UID = generate_random_UID()
    #     self.add_row()




async def create_image_row(file_path : str) -> Union[Images, NoSuchFileError]:
    if check_file_exists(file_path):
        _image = Images(file_path = file_path,
                        UID       = generate_random_UID(),
                        hash      = get_fileHash(file_path),
                        )
        
        try:
            await _image.add_row()
            return _image
        except Exception as e:
            print(f"Error adding product card: {e}")
            return None
    else:
        return NoSuchFileError(file_path)