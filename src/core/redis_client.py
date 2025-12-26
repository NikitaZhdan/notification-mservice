from redis.asyncio import Redis
from src.core.config import settings


redis_connection: Redis | None = None


async def start_redis():
    global redis_connection
    redis_connection = Redis(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=0,
        decode_responses=True,
    )
    print("Redis start")


async def close_redis():
    global redis_connection
    if redis_connection:
        await redis_connection.close()


def get_redis_client() -> Redis:
    if redis_connection is None:
        raise RuntimeError("Redis not initialized")
    return redis_connection
