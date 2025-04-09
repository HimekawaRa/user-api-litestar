from litestar import Litestar
from litestar.openapi.config import OpenAPIConfig
from advanced_alchemy.extensions.litestar.plugins.init_plugin import SQLAlchemyInitPlugin as SQLAlchemyPlugin
from advanced_alchemy.extensions.litestar import AlchemyExtension
from app.routes.user import UserController
from app.config import DATABASE_URL

alchemy_plugin = SQLAlchemyPlugin(connection_string=DATABASE_URL)

app = Litestar(
    route_handlers=[UserController],
    plugins=[alchemy_plugin],
    openapi_config=OpenAPIConfig(title="User API", version="1.0.0"),
    extensions=[AlchemyExtension()]
)
