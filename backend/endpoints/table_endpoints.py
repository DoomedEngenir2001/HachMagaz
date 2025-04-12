
from typing import Annotated
import shutil
import os
from fastapi import APIRouter, Depends, Response, status, FastAPI, File, UploadFile
#-------------------------------------------------------------#
from orm_models.orm_base                import ORM_Base
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
from backend_configuration import Backend_Configuration
#-------------------------------------------------------------#
from objects_DTO.productCard_DTO import ProductCard_DTO
from ORM_dict import ORM_dict
#-------------------------------------------------------------#
from fastapi.security import OAuth2PasswordBearer
from logic.l_jwt      import verify_jwt, create_jwt
#-------------------------------------------------------------#


table_routes = APIRouter()


@table_routes.get("/get_table_data")
async def get_table_data(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].get_table_data()
    else:
        return {"message": "Table not found"}

@table_routes.get("/get_table_row_data")
async def get_table_row_data(table : str, rowId : int):
    if table in ORM_dict.keys():
        _return : ORM_Base = await ORM_Base.get_rowById(ORM_dict[table], rowId)
        return _return.toDict()
    else:
        return {"message": "Table not found"}

@table_routes.get("/drop_table")
async def drop_table(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].drop_table()
    else:
        return {"message": "Table not found"}

@table_routes.get("/drop_all_tables_data")
async def drop_table_data():
    for table in ORM_dict.keys():
        await ORM_dict[table].drop_table_data()
    return {"message": "All tables data dropped"}

@table_routes.get("/drop_table_data")
async def drop_table_data(table : str):
    if table in ORM_dict.keys():
        return await ORM_dict[table].drop_table_data()
    else:
        return {"message": "Table not found"}
    
@table_routes.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(Backend_Configuration.IMAGES_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  # Сохраняем файл

    return {"filename": file.filename, "path": file_path}

