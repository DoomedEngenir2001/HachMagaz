#-------------------------------------------------------------#
from JWT_configuration import JWT_Configuration
import jwt
import datetime
#-------------------------------------------------------------#
from fastapi import FastAPI, Depends, HTTPException
#-------------------------------------------------------------#

async def create_jwt(user_id: int):
    print(user_id)
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=JWT_Configuration.VALIDITY_TIME)  # Токен на 1 час
    }
    token = jwt.encode(payload, JWT_Configuration.SECRET_KEY, algorithm=JWT_Configuration.ALGORITHM)
    return token

async def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, JWT_Configuration.SECRET_KEY, algorithms=[JWT_Configuration.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
