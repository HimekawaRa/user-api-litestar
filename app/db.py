from advanced_alchemy.config import SQLAlchemyAsyncConfig
from litestar.contrib.sqlalchemy.plugins import SQLAlchemyPlugin

from app.models import Base

sqlalchemy_config = SQLAlchemyPlugin(
    config=SQLAlchemyAsyncConfig(
        connection_string="postgresql+psycopg://postgres:postgres@localhost:5432/postgres",
        metadata=Base.metadata  # ✅ Важно для миграций
    )
)