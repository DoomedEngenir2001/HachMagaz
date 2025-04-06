
from typing import Annotated
import shutil
import os
from fastapi import APIRouter, Depends, Response, status, FastAPI, File, UploadFile
#-------------------------------------------------------------#
#ORM models block №1
from orm_models.orm_products            import Products 
from orm_models.orm_images              import Images
from orm_models.orm_productCards        import ProductCards
#ORM models block №2
from orm_models.orm_users              import Users
from orm_models.orm_orders             import Orders
from orm_models.orm_transactions       import Transactions
#-------------------------------------------------------------#
from orm_models.orm_configuration import ORM_Configuration
from backend_configuration import Backend_Configuration
#-------------------------------------------------------------#
from objects_DTO.productCard_DTO import ProductCard_DTO
from ORM_dict import ORM_dict
#-------------------------------------------------------------#


productCards_routes = APIRouter()

@productCards_routes.get("/getProductCard")
async def get_product_card(product_id: int):
    return await ProductCards.get_rowById(cls=ProductCards, id=product_id)

@productCards_routes.get("/getProductCards")
async def get_product_card():
    cards : list = await ProductCards.get_table_data()
    for index, card in enumerate(cards):
        card : ProductCards
        cards[index] =  ProductCard_DTO(card)
        await cards[index].get_image()
    return cards
