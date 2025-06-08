
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
from logic.l_products import create_product_row
from logic.l_images import create_image_row
from ORM_dict import ORM_dict
from pydantic import BaseModel
#-------------------------------------------------------------#
from store.s3client import S3Client
from store.store_config import ACCESS_KEY, SECRET_KEY, URL, BUCKET
from datetime import date
from logic.l_images import create_image_row
import base64
from logic.l_jwt import verify_request

CARD_BATCH=8
S3CONTAINER = "058fc2e1-e870-47c5-9f35-bc8a2df28ab2"
productCards_routes = APIRouter()
class addCardRequest(BaseModel):
    description: str
    image: str
    price: int
    product: str
    limit: int

class editCardRequest(BaseModel):
    id: int
    description: str
    image: str
    price: int
    product: str
    limit: int

class deleteCardRequest(BaseModel):
    id: int

class ImageRequest(BaseModel):
    content: str
    filename: str

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
        try:
            card = ProductCard_DTO(card)
            await card.get_image()
            response.append(card)
        except IndexError:
            pass
    return response

@productCards_routes.post("/processImage")
async def process_image(req:ImageRequest, auth=Depends(verify_request))->dict:
    client = S3Client(ACCESS_KEY, SECRET_KEY, URL, BUCKET)
    content = base64.b64decode(req.content.encode('utf-8'))
    await client.upload(content, req.filename)
    filepath = f"https://{S3CONTAINER}.selstorage.ru/images%2F{req.filename}"
    await create_image_row(filepath)
    return{"filename":filepath}

@productCards_routes.post("/addCard")
async def add_product_card(req: addCardRequest, auth=Depends(verify_request))->dict:
    # Cначала нужно сохранить картинку в файловой системе, только потом запись в бд делать
    product = await create_product_row(title=req.product, description=req.description, price=req.price, countInStock=req.limit)
    image = await create_image_row(file_path=req.image)
    if(isinstance(product, Products) and isinstance(image, Images)):
        await create_productCard_row(product_id=product.id,
                                    image_id=image.id,
                                    title=product.title,
                                    description=product.description,
                                    specPrice=product.price,
                                    limit=product.countInStock)
        return {"status":"success"}
    else:
        return {"message": "failed"}

@productCards_routes.post("/editCard")
async def edit_product_card(req: editCardRequest, auth=Depends(verify_request))->dict:
    await ProductCards.update_product_card(req.id, 2, req.product, req.description, req.price, req.limit)
    return {"status":"success"}