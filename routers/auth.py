from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os

import cruds.auth as auth_crud

router = APIRouter()

@router.post("/login")
async def login():
    pass

@router.post("/me")
async def me():
    pass

@router.post("/logout")
async def logout():
    pass
