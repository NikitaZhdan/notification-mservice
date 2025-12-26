from redis.asyncio import Redis
from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.notifications.repositories import NotificationRepository
from src.notifications.schemas import NotificationBase, NotificationResponse
from src.notifications.cache import NotificationCache
from src.core.config import settings
from src.messaging.producer import publish_notification


class NotificationService:
    def __init__(self, session: AsyncSession, redis: Redis):
        self.notification_repo = NotificationRepository(session)
        self.notification_cache = NotificationCache(redis)


    async def create_notification(self, notification_data: NotificationBase) -> NotificationResponse:
        if await self.notification_cache.get_idem_key(notification_data.idempotency_key):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)

        if await self.notification_repo.get_by_idempotency_key(notification_data.idempotency_key):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        notification = await self.notification_repo.create(notification_data)

        await publish_notification(notification.id, notification.payload)

        await self.notification_cache.set_idem_key(
            notification.id,
            notification_data.idempotency_key,
            ttl=settings.KEY_TTL
        )

        return NotificationResponse(
            recipient=notification.recipient,
            status=notification.status
        )