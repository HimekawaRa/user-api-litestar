
from msgspec import Struct
from datetime import datetime

class UserSchema(Struct, kw_only=True):
    id: int | None = None
    name: str
    surname: str
    password: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

