from msgspec import Struct

class UserBase(Struct):
    name: str
    surname: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
    created_at: str
    updated_at: str

class UserUpdate(Struct, omit_defaults=True):
    name: str | None = None
    surname: str | None = None
    password: str | None = None
