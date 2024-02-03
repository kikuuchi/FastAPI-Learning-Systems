from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

import cruds.auth as auth_crud
import schemas.auth as auth_schema

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

# トークンを検証してユーザを取得
def get_current_user(request: Request, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # エラーメッセージの作成
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        # トークンをデコードしてペイロードを取得
        payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=['HS256'])
        # トークンに紐づくユーザ情報の取得
        user = auth_crud.getUserById(db, payload['user_id'])
        if not user:
            # トークンに紐づくユーザ情報が取得できなかった場合
            raise credentials_exception
        return user
    except JWTError:
        # jwt でエラーが発生した場合
        raise credentials_exception

# ログインAPI
@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth_crud.getUser(db, mail=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail=f'メールアドレスまたはパスワードが違います。')
    return create_tokens(user.id)

@router.post("/me")
async def me():
    pass

@router.post("/logout")
async def logout():
    pass
