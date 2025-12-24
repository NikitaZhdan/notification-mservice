from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.dependencies import main_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield


app = FastAPI()
app.include_router(main_router)
