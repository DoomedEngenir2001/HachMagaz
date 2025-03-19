#-------------------------------------------------------------#
from project_init import init
init()
#-------------------------------------------------------------#
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from orm_models.orm_products import Products
from orm_models.session_handler import get_session
#-------------------------------------------------------------#

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}