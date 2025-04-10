from litestar import get, post, put, delete, Router
from litestar.exceptions import HTTPException
from app.models import User
from app.schemas import UserSchema
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from sqlalchemy.future import select
from app.config import DATABASE_URL

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)
Session = async_sessionmaker(engine)

@post("/users")
async def create_user(data: UserSchema) -> UserSchema:
    new_user = User(name=data.name, surname=data.surname, password=data.password)
    async with Session() as session:
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
    return UserSchema(**new_user.__dict__)

@get("/users")
async def list_users() -> list[UserSchema]:
    async with Session() as session:
        result = await session.execute(select(User))
        return [UserSchema(**u.__dict__) for u in result.scalars().all()]

@get("/users/{user_id:int}")
async def get_user(user_id: int) -> UserSchema:
    async with Session() as session:
        user = await session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Not found")
    return UserSchema(**user.__dict__)

@put("/users/{user_id:int}")
async def update_user(user_id: int, data: UserSchema) -> UserSchema:
    async with Session() as session:
        user = await session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Not found")
        user.name = data.name
        user.surname = data.surname
        user.password = data.password
        await session.commit()
        await session.refresh(user)
    return UserSchema(**user.__dict__)

@delete("/users/{user_id:int}", status_code=200)
async def delete_user(user_id: int) -> dict:
    async with Session() as session:
        user = await session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Not found")
        await session.delete(user)
        await session.commit()
    return {"detail": "User deleted"}

user_router = Router(path="/", route_handlers=[create_user, list_users, get_user, update_user, delete_user])
