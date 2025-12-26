from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.session import get_session
from src.notifications.services import NotificationService
from redis.asyncio import Redis
from src.core.redis_client import get_redis_client


async def get_notification_service(
    session: AsyncSession = Depends(get_session),
    redis: Redis = Depends(get_redis_client),
) -> NotificationService:
    return NotificationService(session, redis)
