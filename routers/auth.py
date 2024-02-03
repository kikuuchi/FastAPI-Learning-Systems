from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

import cruds.auth as auth_crud

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# パスワード認証を行い、トークンを生成
def create_tokens(user_id: int):
    # ペイロード作成
    access_payload = {
        'token_type': 'access_token',
        'exp': datetime.utcnow() + timedelta(minutes=60),
        'user_id': user_id
    }
    access_token = jwt.encode(access_payload, os.environ["SECRET_KEY"], algorithm='HS256')
    return{'access_token': access_token, 'token_type': 'bearer'}
@router.post("/login")
async def login():
    pass

@router.post("/me")
async def me():
    pass

@router.post("/logout")
async def logout():
    pass
