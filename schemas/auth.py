from typing import Optional
from pydantic import BaseModel

# ログインユーザ  レスポンススキーマ
class loginUser(BaseModel):
    id: int
    user_name: Optional[str]

    class Config:
        orm_mode=True
