#-------------------------------------------------------------#
from typing import Union
#-------------------------------------------------------------#
from orm_models.orm_products      import Products
from orm_models.orm_images        import Images
from orm_models.orm_productCards  import ProductCards
from orm_models.orm_base          import ORM_Base
#-------------------------------------------------------------#
from l_errors                 import NoSuchFileError
#-------------------------------------------------------------#
from side_methods             import check_file_exists, generate_random_UID
#-------------------------------------------------------------#
from hash_methods             import get_fileHash
#-------------------------------------------------------------#

    # product_id  = Column(Integer,     ForeignKey(f"{ORM_Configuration.t_products}.id"),
    #                         index=True, nullable=False)
    # image_id    = Column(Integer,     ForeignKey(f"{ORM_Configuration.t_images}.id"),
    #                         index=True, nullable=False)
    # title       = Column(String(255), index=True, default=ORM_Base.str_None)
    # description = Column(String(255), index=True, default=ORM_Base.str_None)
    # specPrice   = Column(Integer,     index=True, default=ORM_Base.int_None)
    # limit       = Column(Integer,     index=True, default=ORM_Base.int_None)


async def create_productCard_row(product_id : int,
                                 image_id   : int,
                                 title      : str,
                                 description: str,
                                 specPrice  : int,
                                 limit      : int) -> ProductCards:
    

    _productCard = ProductCards(product_id   = product_id,
                                image_id     = image_id,
                                title        = title,
                                description  = description,
                                specPrice    = specPrice,
                                limit        = limit,
                                product      = await Products.get_rowById(Products, product_id),
                                image        = await Images.get_rowById(Images, image_id),   
                                )
    try:
        await _productCard.add_row()
        return _productCard
    except Exception as e:
        print(f"Error adding product card: {e}")
        return None