from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.base_router import main_router
from src.core.redis_client import start_redis, close_redis
from src.core.rabbit_client import init_rabbit, close_rabbit


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_rabbit()
    await start_redis()

    yield

    await close_rabbit()
    await close_redis()


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)
