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
from l_errors import UniqueDataError
#-------------------------------------------------------------#


async def create_user(  login    : str,
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

    _user = Users(login    = login,
                  hashPassword = hash_password(password)[0],
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