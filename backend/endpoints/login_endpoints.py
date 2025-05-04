from typing import Annotated
from pydantic import BaseModel
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
from orm_models.test_data_loader import insert_images_data, insert_products_data, insert_productCards_data, insert_users_data
#-------------------------------------------------------------#
from fastapi.security import OAuth2PasswordBearer
from logic.l_jwt      import verify_jwt, create_jwt
#-------------------------------------------------------------#

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
login_router = APIRouter()
class login_req(BaseModel):
    login: str
    password: str
@login_router.post("/login")
async def login(req: login_req) -> str:
    user = await Users.get_rowByLogin(cls=Users, login=req.login)
    if isinstance(user, Users):
        print( type(req.password) , req.password)
        if await user.verify_password(req.password):
            return {"token": await create_jwt(user.id) }
        else:
            return {"error": "Authentication failed"}
    else:
        return {"error": "User not found"}
