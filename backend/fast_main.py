#-------------------------------------------------------------#
from project_init import init
init()
#-------------------------------------------------------------#
from fastapi import FastAPI
#-------------------------------------------------------------#
from endpoints.base_endpoints import router
from endpoints.table_endpoints import table_routes
from endpoints.productCard_endpoints import productCards_routes
#-------------------------------------------------------------#

app = FastAPI()
app.include_router(router)
app.include_router(table_routes)
app.include_router(productCards_routes)

