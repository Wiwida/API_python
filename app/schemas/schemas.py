from pydantic import BaseModel
from typing import Union


class Travellers(BaseModel):
    UIC: int
    Gare: str
    CSP: str
    Pourcentage: float
    Annee: int


class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
