
from typing import Annotated
from typing import Any
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
from side_methods import get_current_datetime
#-------------------------------------------------------------#
from objects_DTO.productCard_DTO import ProductCard_DTO
from ORM_dict import ORM_dict
from pydantic import BaseModel
#-------------------------------------------------------------#
from logic.l_errors   import UniqueDataError, AuthenticationError
from logic.l_users    import  create_user_row_reg, authenticate_user
from logic.l_jwt      import verify_jwt, create_jwt
#-------------------------------------------------------------#
class sign_up_request(BaseModel):
    login: str
    password: str
    email: str
    phone: str
  
class login_req(BaseModel):
    login: str
    password: str

user_routes = APIRouter()


@user_routes.post("/registration")
async def create_user(   req: sign_up_request)->dict: # ДОДЕЛАТЬ
    _result = await create_user_row_reg( login=req.login, password=req.password, 
                                    email=req.email, phone=req.phone)
    if isinstance(_result, UniqueDataError):
        return {"message": _result.show()}
    elif isinstance(_result, str):
        token = await create_jwt( _result)
        return {"token":token}
    
@user_routes.post("/login")
async def login_user(req:login_req
                     #, email: str = None, phone: str = None
                     ):
    # print(f"login_user: {password}, {login}, {email}, {phone}")
   # user : Users = None
    if req.login is not None:
        user = await Users.get_rowByLogin( req.login )
    # elif email is not None:
    #     user = await Users.get_rowByEmail( email )
    # elif phone is not None:
    #     user = await Users.get_rowByPhone( phone )
        if isinstance(user, Users):
            token = await authenticate_user(user, _inputPassword=req.password)
            if isinstance(token, str):
                # TODO: Сделать обновление последнего входа в систему
                # TODO: user вываливается из сессии, нужно обновить его
                token = await create_jwt(user.login)
                # await user.update_last_seen()
                return {"token": token}
            elif isinstance(token, AuthenticationError):
                return AuthenticationError("Invalid password").show
        
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
        return user.toDict()
    else:
        return {"message": "User not found"}

# TODO: Что то не так с этой функцией
