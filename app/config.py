import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/postgres"