
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
from objects_DTO.order_DTO import Order_DTO
from ORM_dict import ORM_dict
from orm_models.orm_base         import ORM_Base
from orm_models.orders_status    import Order_status
from orm_models.test_data_loader import insert_images_data, insert_products_data, insert_productCards_data, insert_users_data
#-------------------------------------------------------------#
from fastapi.security      import OAuth2PasswordBearer
from logic.l_jwt           import verify_jwt, create_jwt
from logic.l_transanctions import create_transaction_row
from logic.l_orders        import create_order_row
from pydantic import BaseModel
from yookassa import Payment, Configuration
import uuid
#-------------------------------------------------------------#
Configuration.account_id = "1096384"
Configuration.secret_key = "test_o1MqMgM5oiWYOtdjR3YNwkbprns3GMb1Lc-CqOPeRGA"
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
    bill: int
    method: str

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
                    if isinstance(_order, Orders):
                        if req.method == 'bank_card':
                            payment = Payment.create({
                                "amount": {
                                "value": "%.02f" %req.bill,
                                "currency": "RUB"
                                },
                                "payment_method_data": {
                                    "type": req.method
                                },
                                "confirmation": {
                                "type": "redirect",
                                "return_url": "http://localhost:5173/"
                                },
                                "capture": True,
                                "description": f"Заказ №{_order.id}",
                                })
                                # get confirmation
                            confirmation_url = payment.confirmation.confirmation_url
                        if req.method == "Nal":
                            confirmation_url = "http://localhost:5173/"
                        _transactions : Transactions = await create_transaction_row(
                                                                order_id       = _order.id,
                                                                productCard_id = _productCard.id,
                                                                count          = int(req.count[i]),
                                                                price          = _productCard.specPrice,
                                                                bankCardInfo   = ORM_Base.str_None,
                                                                )
                        return {"url": confirmation_url}
                    
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
async def get_order_for_user_with_status(user_id: int = None, status : str = Order_status.STATUS_CREATED):
    try:
        _orders : Orders = await Orders.get_user_orders(user_id)
        print( "_orders : " +  _orders.__repr__() )
        orders:list = []
        for _order in _orders:
            order = Order_DTO(_order)
            orders.append(order)
        return orders
    except Exception as e:
        return {"error":e}
