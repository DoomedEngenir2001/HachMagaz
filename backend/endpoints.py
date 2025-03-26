
from typing import Annotated
import shutil
import os
from fastapi import APIRouter, Depends, Response, status, FastAPI, File, UploadFile
from orm_models.orm_products import Products
from orm_models.orm_productCards import ProductCards
from orm_models.orm_images import Images
from orm_models.orm_configuration import ORM_Configuration
from backend_configuration import Backend_Configuration
#-------------------------------------------------------------#
from objects_DTO.productCard_DTO import ProductCard_DTO
#-------------------------------------------------------------#

ORM_dict = {
        ORM_Configuration.t_products      : Products,
        ORM_Configuration.t_productsCards : ProductCards,
        ORM_Configuration.t_images        : Images
    }

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Иди нахуй"}

@router.get("/get_table_data")
async def get_table_data(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].get_table_data()
    else:
        return {"message": "Table not found"}

@router.get("/drop_table")
async def drop_table(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].drop_table()
    else:
        return {"message": "Table not found"}

@router.get("/drop_table_data")
async def drop_table_data(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].drop_table_data()
    else:
        return {"message": "Table not found"}

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(Backend_Configuration.IMAGES_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  # Сохраняем файл

    return {"filename": file.filename, "path": file_path}

@router.get("/getProductCard")
async def get_product_card(product_id: int):
    return await ProductCards.get_rowById(cls=ProductCards, id=product_id)

@router.get("/getProductCards")
async def get_product_card():
    cards : list = await ProductCards.get_table_data()
    for index, card in enumerate(cards):
        card : ProductCards
        cards[index] =  ProductCard_DTO(card)
        await cards[index].get_image()
    return cards


