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
#-------------------------------------------------------------#

ORM_dict = {
        ORM_Configuration.t_products      : Products,
        ORM_Configuration.t_productsCards : ProductCards,
        ORM_Configuration.t_images        : Images,
        ORM_Configuration.t_users         : Users,
        ORM_Configuration.t_orders        : Orders,
        ORM_Configuration.t_transactions  : Transactions,
    }