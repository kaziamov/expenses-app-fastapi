import os
import random
from string import ascii_letters, digits

from dotenv import load_dotenv


load_dotenv()


production = "production"


BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_DOMAIN = os.getenv("WEBHOOK_DOMAIN")
ENVIROMENT = str(os.getenv("ENVIROMENT"))

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT"))
POSTGRES_DB = os.getenv("POSTGRES_DB")

if "railway" in ENVIROMENT:
    POSTGRES_USER = os.getenv("PGUSER")
    POSTGRES_PASSWORD = os.getenv("PGPASSWORD")
    POSTGRES_HOST = os.getenv("PGHOST")
    POSTGRES_PORT = int(os.getenv("PGPORT"))
    POSTGRES_DB = os.getenv("PGDATABASE")

# Optional
RANDON_WEBHOOK_PATH = "".join(random.choices(list(ascii_letters + digits), k=32))
WEBHOOK_PATH = os.getenv("WEBHOOK_PATH", f"webhook/{RANDON_WEBHOOK_PATH}")

APP_PORT = os.getenv("APP_PORT")
APP_HOST = os.getenv("APP_HOST")

CACHE_SIZE = int(os.getenv("CACHE_SIZE", 100))

# Automatic generated
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
ASYNC_DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


# Test env
ASYNC_TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres_test"
# ASYNC_TEST_DATABASE_URL = "sqlite:///./test.db"


# Flags
FLAG__NOT_PRODUCTION = ENVIROMENT != production
