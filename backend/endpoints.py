
from typing import Annotated

from fastapi import APIRouter, Depends, Response, status
from orm_models.orm_products import Products
from orm_models.orm_productCards import ProductCards
from orm_models.orm_images import Images
from orm_models.orm_configuration import ORM_Configuration


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
async def drop_products_table(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].drop_table()
    else:
        return {"message": "Table not found"}

@router.get("/drop_table_data")
async def drop_products_data(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].drop_table_data()
    else:
        return {"message": "Table not found"}

