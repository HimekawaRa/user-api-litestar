from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from app.routes import user_router

openapi_config = OpenAPIConfig(
    title="Litestar User API",
    version="0.1.0",
    description="REST API для управления пользователями",
    contact={"name": "Raul"},
)

app = Litestar(
    route_handlers=[user_router],
    openapi_config=openapi_config,
)
