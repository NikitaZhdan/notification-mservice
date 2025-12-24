from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models import Notification
from src.notifications.schemas import NotificationBase
from uuid import UUID


class NotificationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, notification_data: NotificationBase) -> Notification:
        stmt = Notification(
            type=notification_data.type,
            recipient=notification_data.recipient,
            payload=notification_data.payload,
            idempotency_key=notification_data.idempotency_key,
        )

        self.session.add(stmt)
        await self.session.commit()

        return stmt

    async def get_by_idempotency_key(self, idempotency_key: UUID) -> Notification | None:
        stmt = select(Notification).where(Notification.idempotency_key == idempotency_key)
        result = await self.session.execute(stmt)

        return result.scalar_one_or_none()
