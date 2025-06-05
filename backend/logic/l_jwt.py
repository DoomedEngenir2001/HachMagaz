#-------------------------------------------------------------#
from JWT_configuration import JWT_Configuration
import jwt
import datetime
from fastapi import Request
#-------------------------------------------------------------#
from fastapi import FastAPI,  HTTPException
#-------------------------------------------------------------#

async def create_jwt(login: str):
    payload = {
        "user_id": login,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=JWT_Configuration.VALIDITY_TIME)  # Токен на 1 час
    }
    token = jwt.encode(payload, JWT_Configuration.SECRET_KEY, algorithm=JWT_Configuration.ALGORITHM)
    return token

async def verify_jwt(token: str):
    try:
        payload = jwt.decode(token, JWT_Configuration.SECRET_KEY, algorithms=[JWT_Configuration.ALGORITHM])
        return True
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
async def verify_request(req: Request):
    print(req.headers)
    auth_header = req.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401, detail="Missing Authorization header")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    token = auth_header[len("Bearer "):]
    print(token)
    return verify_jwt(token)