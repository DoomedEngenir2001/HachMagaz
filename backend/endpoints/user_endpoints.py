
from typing import Annotated
import shutil
import os
from fastapi.security import OAuth2PasswordBearer
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
from logic.l_errors   import UniqueDataError, AuthenticationError
from logic.l_users    import create_user_row
from logic.l_jwt      import verify_jwt, create_jwt
#-------------------------------------------------------------#


user_routes = APIRouter()


@user_routes.get("/create_user")
async def get_table_data(   login    : str,
                            password : str,
                            email    : str,
                            phone    : str,):
    _result = await create_user_row( login=login, password=password, email=email, phone=phone )

    if isinstance(_result, UniqueDataError):
        return {"message": _result.show}
    elif isinstance(_result, tuple):
        return {"user_id": _result[0].id, "order_id": _result[1].id}
    
@user_routes.get("/is_user_exist")
async def is_user_exist(login: str = None, email: str = None, phone: str = None):
    _result : bool = False
    if login is not None:
        _result = _result or await Users.is_login_exist(login)
    if email is not None:
        _result = _result or await Users.is_email_exist(email)
    if phone is not None:
        _result = _result or await Users.is_phone_exist(phone)
    
    return {"message": _result}

@user_routes.get("/get_user")
async def get_user(user_id: int):
    user : Users = await Users.get_rowById(cls=Users, id=user_id)
    if isinstance(user, Users):
        return user.__dict__()
    else:
        return {"message": "User not found"}

