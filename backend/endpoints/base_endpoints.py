
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
from fastapi.security import OAuth2PasswordBearer
from logic.l_jwt      import verify_jwt, create_jwt
#-------------------------------------------------------------#

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Иди нахуй"}

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

@router.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    user_data = await verify_jwt(token)
    return {"message": "Вы получили доступ!", "user_id": user_data["user_id"]}

@router.get("/get_user_JWT_token")
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
