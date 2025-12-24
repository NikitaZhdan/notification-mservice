from fastapi import status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Notification
from src.notifications.repositories import NotificationRepository
from src.notifications.schemas import NotificationBase, NotificationResponse


class NotificationService:
    def __init__(self, session: AsyncSession):
        self.notification_repo = NotificationRepository(session)


    async def create_notification(self, notification_data: NotificationBase) -> NotificationResponse:
        if self.notification_repo.get_by_idempotency_key(notification_data.idempotency_key):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)

        await self.notification_repo.create(notification_data)

        return NotificationResponse(
            recipient=notification_data.recipient,
            status=notification_data.status
        )