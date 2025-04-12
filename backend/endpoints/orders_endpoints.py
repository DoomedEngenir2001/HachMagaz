
from typing import Annotated
import shutil
import os
from fastapi import APIRouter, Depends, Response, status, FastAPI, File, UploadFile
#-------------------------------------------------------------#
#ORM models block №1
from orm_models.orm_products           import Products 
from orm_models.orm_images             import Images
from orm_models.orm_productCards       import ProductCards
#ORM models block №2
from orm_models.orm_users              import Users
from orm_models.orm_orders             import Orders
from orm_models.orm_transactions       import Transactions
#-------------------------------------------------------------#
from orm_models.orm_configuration import ORM_Configuration
from backend_configuration        import Backend_Configuration
#-------------------------------------------------------------#
from objects_DTO.productCard_DTO import ProductCard_DTO
from ORM_dict import ORM_dict
from orm_models.test_data_loader import insert_images_data, insert_products_data, insert_productCards_data, insert_users_data
#-------------------------------------------------------------#
from fastapi.security import OAuth2PasswordBearer
from logic.l_jwt      import verify_jwt, create_jwt
#-------------------------------------------------------------#

orders_router = APIRouter()

@orders_router.get_orders_for_user("/get_orders_for_user")
async def get_orders_for_user(login: str = None, email: str = None, phone: str = None):
    pass
