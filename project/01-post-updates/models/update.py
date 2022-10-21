from pydantic import BaseModel


class UserUpdateIn(BaseModel):
    body: str
    user_id: int


class UserUpdate(UserUpdateIn):
    id: int


class UserIn(BaseModel):
    name: str
    password: str


class UserOut(BaseModel):
    id: int
    name: str
