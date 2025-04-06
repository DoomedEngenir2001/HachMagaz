
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
from orm_models.test_data_loader import insert_images_data, insert_products_data, insert_productCards_data, insert_users_data
#-------------------------------------------------------------#
from fastapi.security import OAuth2PasswordBearer
from logic.l_jwt      import verify_jwt, create_jwt
#-------------------------------------------------------------#

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


debug_router = APIRouter()

@debug_router.get("/")
async def root():
    return {"message": "Иди нахуй"}


@debug_router.get("/setup_debug_data")
async def setup_debug_data():
    imagesList   = await insert_images_data()
    productsList = await insert_products_data()
    print ("productsList", productsList)
    print ("imagesList", imagesList)
    productCardsList = await insert_productCards_data(productsList, imagesList)
    usersList = await insert_users_data()
    return {"images": imagesList, 
            "products": productsList, 
            "productCards": productCardsList, 
            "users": usersList}

@debug_router.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    user_data = await verify_jwt(token)
    return {"message": "Вы получили доступ!", "user_id": user_data["user_id"]}

@debug_router.get("/get_user_JWT_token")
async def get_user_JWT_token(user_id: int, password: str):
    user = await Users.get_rowById(cls=Users, id=user_id)
    if isinstance(user, Users):
        print( type(password) , password)
        if await user.verify_password(password):
            return {"token": await create_jwt(user.id)}
        else:
            return {"error": "Authentication failed"}
    else:
        return {"error": "User not found"}
