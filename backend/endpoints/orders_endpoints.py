
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
from objects_DTO import order_DTO
from ORM_dict import ORM_dict
from orm_models.orm_base         import ORM_Base
from orm_models.orders_status    import Order_status
from orm_models.test_data_loader import insert_images_data, insert_products_data, insert_productCards_data, insert_users_data
#-------------------------------------------------------------#
from fastapi.security      import OAuth2PasswordBearer
from logic.l_jwt           import verify_jwt, create_jwt
from logic.l_transanctions import create_transaction_row
from logic.l_users         import get_user_orders, get_user_orders_with_status
from logic.l_orders        import create_order_row
from pydantic import BaseModel
#-------------------------------------------------------------#

orders_router = APIRouter()

# @orders_router.get_orders_for_user("/get_orders_for_user")
# async def get_orders_for_user(login: str = None, email: str = None, phone: str = None):
#     pass


# /addToCart - рут
# Запрос
# {
# login: String,
# count:Number,
# price:Number,
# product:String
# }
class order_reg(BaseModel):
    user_id: int
    address: str
    productCard_ids: list
    count: list

@orders_router.post("/newOrder")
async def add_to_order(req: order_reg)->dict:
    _user = await Users.get_rowById(Users, req.user_id)
    _order: Orders =  await create_order_row(req.user_id, _user.email, _user.phone,req.address)
    if isinstance(_user, Users):
        for i, productCard_id in enumerate(req.productCard_ids):
            print(productCard_id)
            _productCard = await ProductCards.get_rowById(ProductCards, int(productCard_id))
            if isinstance(_productCard, ProductCards):
                if req.count[i] <= _productCard.limit:
                    #_order : Orders = await get_user_orders_with_status(req.user_id, Order_status.STATUS_CREATED)
                    # print( "_order result : " + str(_order) )
                    if isinstance(_order, Orders):
                        _transactions : Transactions = await create_transaction_row(
                                                            order_id       = _order.id,
                                                            productCard_id = _productCard.id,
                                                            count          = int(req.count[i]),
                                                            price          = _productCard.specPrice,
                                                            bankCardInfo   = ORM_Base.str_None,
                                                            )
                    
                    # print( "_transactions result : " + str(_transactions) )
                else:
                    return {"message": "Order not found"}
            else:
                return {"message": "Limit exceeded"}
        else:
            return {"message": "Product card not found"}
    else:
        return {"message": "User not found"}

@orders_router.get("/get_order_for_user_with_status")
async def get_order_for_user_with_status(user_id: int = None, login : str = None, status : str = Order_status.STATUS_CREATED)->list:
    _user : Users = None
    if user_id is not None:
        _user = await Users.get_rowById(Users, user_id)
    if login is not None:
        _user = await Users.get_rowByLogin( login )

    print( "_user : " +  _user.__repr__() )

    if isinstance(_user, Users) and status in Order_status.get_all_statuses():
        _orders : Orders = await get_user_orders(_user.id)
        print( "_orders : " +  _orders.__repr__() )
        if isinstance(_orders, Orders):
            orders = []
            for _order in _orders:
                order = order_DTO(_order)
                orders.append(order)
            return orders
        else:
            return {"message": "Orders not found"}