#-------------------------------------------------------------#
from project_init import init
init(True)
#-------------------------------------------------------------#
from orm_models.orm_products            import Products 
from orm_models.orm_images              import Images
from orm_models.orm_productCards        import ProductCards
#-------------------------------------------------------------#
import asyncio
from db_modules import tables_creator

if __name__ == "__main__":
    tables_creator.create_tables(debug=True)