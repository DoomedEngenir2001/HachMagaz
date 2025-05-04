#-------------------------------------------------------------#
from typing import Union
#-------------------------------------------------------------#
from orm_models.orm_users     import Users
from orm_models.orm_orders    import Orders
from orm_models.orders_status import Order_status
from orm_models.orm_base      import ORM_Base
#-------------------------------------------------------------#
from hash_methods import hash_password, verify_password
from side_methods import get_current_datetime
#-------------------------------------------------------------#
from l_errors import UniqueDataError, AuthenticationError
#-------------------------------------------------------------#
from l_jwt import create_jwt
#-------------------------------------------------------------#


async def create_user_row(  login    : str,
                            password : str,
                            email    : str,
                            phone    : str,
                            ) -> Union[UniqueDataError, tuple[Users, Orders]]:
                
    
    if await Users.is_login_exist(login):
        return UniqueDataError("login")
    if await Users.is_email_exist(email):
        return UniqueDataError("email")
    if await Users.is_phone_exist(phone):
        return UniqueDataError("phone")

    _hash        = hash_password(password)
    hashPassword = _hash[1] + ":" + _hash[0]

    _user = Users(login    = login,
                  hashPassword = hashPassword,
                  email    = email,
                  phone    = phone)
    await _user.add_row()

    _order = Orders(user_id      = _user.id,
                   email        = _user.email,
                   phone        = _user.phone,
                   address      = ORM_Base.str_None,
                   createTime   = get_current_datetime(),
                   status       = Order_status.STATUS_CREATED,
                   user         = _user
                   )

    await _order.add_row()

    return (_user, _order)




async def create_user_row_reg(  login    : str,
                            password : str,
                            email    : str,
                            phone    : str,
                            ) -> str:
                
    
    if await Users.is_login_exist(login):
        return UniqueDataError("login")
    if await Users.is_email_exist(email):
        return UniqueDataError("email")
    if await Users.is_phone_exist(phone):
        return UniqueDataError("phone")

    _hash        = hash_password(password)
    hashPassword = _hash[1] + ":" + _hash[0]

    _user = Users(login    = login,
                  hashPassword = hashPassword,
                  email    = email,
                  phone    = phone)
    await _user.add_row()

    _order = Orders(user_id      = _user.id,
                   email        = _user.email,
                   phone        = _user.phone,
                   address      = ORM_Base.str_None,
                   createTime   = get_current_datetime(),
                   status       = Order_status.STATUS_CREATED,
                   user         = _user
                   )

    await _order.add_row()

    return _user.login

async def authenticate_user(_user : Users, _inputPassword : str) -> Union[AuthenticationError, str]:
    if await _user.verify_password(_inputPassword):
        return await create_jwt(_user.id)
    else:
        return AuthenticationError(_inputPassword)
    
async def get_user_orders(user_id: int) -> Union[Orders, None]:
    _user : Users = await Users.get_rowById(Users, user_id)
    if isinstance(_user, Users):
        return _user.orders
    else:
        return None

async def get_user_orders_with_status(user_id: int, status: str) -> Union[Orders, None]:
    _user : Users = await Users.get_rowById(Users, user_id)
    if isinstance(_user, Users):
        result = await Orders.get_user_orders_with_current_status(_user.id, status)
        # print( "Upper result : " + str(result))
        return result
    else:
        return None