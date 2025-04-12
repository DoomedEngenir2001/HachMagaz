#-------------------------------------------------------------#
from typing import Union
#-------------------------------------------------------------#
from orm_models.orm_orders        import Orders
from orm_models.orm_users         import Users
from orm_models.orm_transactions  import Transactions
from orm_models.orm_base          import ORM_Base
#-------------------------------------------------------------#
from orm_models.orders_status     import Order_status
#-------------------------------------------------------------#
from l_errors                 import NoSuchFileError
#-------------------------------------------------------------#
from side_methods             import check_file_exists, generate_random_UID, get_current_datetime
#-------------------------------------------------------------#
from hash_methods             import get_fileHash
#-------------------------------------------------------------#

async def create_order_row(
                            user_id : int,
                            email   : str = None,
                            phone   : str = None,
                            address : str = None,
                          ) -> Orders:
    _user  : Users = await Users.get_rowById(Users, user_id)
    if isinstance(_user, Users):
        if email is None:
            email = _user.email
        if phone is None:
            phone = _user.phone
        if address is None:
            address = ORM_Base.str_None

        _order = Orders(
                        user_id = user_id,
                        email   = email,
                        phone   = phone,
                        address = address,
                        status  = Order_status.STATUS_CREATED,
                        createTime = get_current_datetime(),
                        user    = _user,
                    )
    try:
        await _order.add_row()
        return _order
    except Exception as e:
        print(f"Error adding order: {e}")
        return None
    

