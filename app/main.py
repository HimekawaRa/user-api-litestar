
from litestar import Litestar
from app.routes import user_router

app = Litestar(route_handlers=[user_router])
