from litestar import Controller, post, get, put, delete
from litestar.di import Provide
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate

class UserRepository(SQLAlchemyAsyncRepository[User]):
    model_type = User

class UserController(Controller):
    path = "/users"
    dependencies = {"repo": Provide(UserRepository)}

    @post()
    async def create_user(self, data: UserCreate, repo: UserRepository) -> UserRead:
        user = await repo.add(User(**data.__dict__))
        return UserRead(**user.__dict__)

    @get()
    async def list_users(self, repo: UserRepository) -> list[UserRead]:
        users = await repo.list()
        return [UserRead(**u.__dict__) for u in users]

    @get(path="/{user_id:int}")
    async def get_user(self, user_id: int, repo: UserRepository) -> UserRead:
        user = await repo.get(user_id)
        return UserRead(**user.__dict__)

    @put(path="/{user_id:int}")
    async def update_user(self, user_id: int, data: UserUpdate, repo: UserRepository) -> UserRead:
        user = await repo.update(user_id, data.__dict__)
        return UserRead(**user.__dict__)

    @delete(path="/{user_id:int}")
    async def delete_user(self, user_id: int, repo: UserRepository) -> dict:
        await repo.delete(user_id)
        return {"deleted": True}
