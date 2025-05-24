
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
from logic.l_productCards import create_productCard_row
from ORM_dict import ORM_dict
from pydantic import BaseModel
#-------------------------------------------------------------#
CARD_BATCH=16

productCards_routes = APIRouter()
class addCardRequest(BaseModel):
    description: str
    id: int
    image: str
    price: int
    product: str
    limit: int

class deleteCardRequest(BaseModel):
    id: int

@productCards_routes.get("/get_product_card")
async def get_product_card(product_id: int):
    _productCards = await ProductCards.get_rowById(cls=ProductCards, id=product_id)
    if isinstance(_productCards, ProductCards):
        return _productCards.toDict()
    return {"message": "Product card not found"}

@productCards_routes.get("/get_product_cards")
async def get_product_cards(index: int):
    cards : list = await ProductCards.get_table_data()
    response : list =[]
    for index in range(index, index+CARD_BATCH):
        #card : ProductCards
        try:
            card = ProductCard_DTO(cards[index])
            await card.get_image()
            response.append(card)
        except IndexError:
            return {"Products is ended"}
    return response

@productCards_routes.get("/get_all_product_cards")
async def get_product_cards():
    cards : list = await ProductCards.get_table_data()
    response : list =[]
    for card in cards:
        #card : ProductCards
        try:
            card = ProductCard_DTO(card)
            await card.get_image()
            response.append(card)
        except IndexError:
            pass
    return response

@productCards_routes.post("/addCard")
async def add_product_card(req: addCardRequest)->dict:
    _id = await Images.get_image_id_by_path(req.image)
    await create_productCard_row(req.id,_id,req.product, req.description, req.price, req.limit)
    return {"status":"success"}

@productCards_routes.post("/editCard")
async def edit_product_card(req: addCardRequest)->dict:
    # _id = await Images.get_image_id_by_path(req.image)
    # print("_id", _id)
    await ProductCards.update_product_card(req.id, 2, req.product, req.description, req.price, req.limit)
    return {"status":"success"}