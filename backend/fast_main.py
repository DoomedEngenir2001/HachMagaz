#-------------------------------------------------------------#
from project_init import init
init()
#-------------------------------------------------------------#
from fastapi import FastAPI
#-------------------------------------------------------------#
from endpoints.debug_endpoints       import debug_router
from endpoints.table_endpoints       import table_routes
from endpoints.productCard_endpoints import productCards_routes
from endpoints.user_endpoints        import user_routes
from endpoints.orders_endpoints      import orders_router
#-------------------------------------------------------------#

app = FastAPI()
app.include_router(debug_router)
app.include_router(table_routes)
app.include_router(productCards_routes)
app.include_router(user_routes)
app.include_router(orders_router)

