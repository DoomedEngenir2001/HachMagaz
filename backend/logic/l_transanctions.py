#-------------------------------------------------------------#
from typing import Union
#-------------------------------------------------------------#
from orm_models.orm_orders        import Orders
from orm_models.orm_productCards  import ProductCards
from orm_models.orm_users         import Users
from orm_models.orm_transactions  import Transactions
from orm_models.orm_base          import ORM_Base
#-------------------------------------------------------------#
from l_errors                 import NoSuchFileError
#-------------------------------------------------------------#
from side_methods             import check_file_exists, generate_random_UID
#-------------------------------------------------------------#
from hash_methods             import get_fileHash
#-------------------------------------------------------------#

async def create_transaction_row(
                            order_id       : int,
                            productCard_id : int,
                            count          : int,
                            price          : int,
                            bankCardInfo   : str = None,
                          ) -> Transactions:
    
    _order : Orders = Orders.get_rowById(Orders, order_id)
    if isinstance(_order, Orders):
        _productCard : ProductCards = ProductCards.get_rowById(ProductCards, productCard_id)
        if isinstance(_productCard, ProductCards):
            _transaction = Transactions(
                            order_id       = order_id,
                            productCard_id = productCard_id,
                            count          = count,
                            price          = price,
                            bankCardInfo   = bankCardInfo,
                            order          = _order,
                            productCard    = _productCard,
                        )
            try:
                await _transaction.add_row()
                return _transaction
            except Exception as e:
                print(f"Error adding transaction: {e}")
                return None
        else:
            print("Product card not found")
            return None
    else:
        return None

#     #Связь с таблицей orders
#     order = relationship(ORM_Configuration.c_Orders,
#                                  back_populates=ORM_Configuration.rel_transactions_to_orders)
#     #Связь с таблицей productsCards
#     productCard = relationship(ORM_Configuration.c_ProductCards,
#                                  back_populates=ORM_Configuration.rel_transactions_to_productsCards)
