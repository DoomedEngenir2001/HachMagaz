#-------------------------------------------------------------#
from project_init import init
init()
#-------------------------------------------------------------#
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
#-------------------------------------------------------------#
from endpoints import router
from backend.db_modules.session_handler import get_session
#-------------------------------------------------------------#
from orm_models.orm_products     import Products
from orm_models.orm_images       import Images
from orm_models.orm_productCards import ProductCards
#-------------------------------------------------------------#

app = FastAPI()
app.include_router(router)

