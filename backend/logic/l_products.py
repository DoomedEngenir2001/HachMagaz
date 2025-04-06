#-------------------------------------------------------------#
from typing import Union
#-------------------------------------------------------------#
from orm_models.orm_products  import Products
from orm_models.orm_base      import ORM_Base
#-------------------------------------------------------------#
from l_errors                 import NoSuchFileError
#-------------------------------------------------------------#
from side_methods             import check_file_exists, generate_random_UID
#-------------------------------------------------------------#
from hash_methods             import get_fileHash
#-------------------------------------------------------------#


# title        = Column(String(255),  index=True, default=ORM_Base.str_None)
# description  = Column(String(255),  index=True, default=ORM_Base.str_None)
# price        = Column(Integer,      index=True, default=ORM_Base.int_None)
# countInStock = Column(Integer,      index=True, default=ORM_Base.int_None)


async def create_product_row(title       : str,
                            description  : str,
                            price        : int,
                            countInStock : int) -> Products:
    _product = Products(title        = title,
                        description  = description,
                        price        = price,
                        countInStock = countInStock)
    try:
        await _product.add_row()
        return _product
    except Exception as e:
        print(f"Error adding product card: {e}")
        return None

    