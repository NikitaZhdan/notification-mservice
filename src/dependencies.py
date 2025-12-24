from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.session import get_session
from src.notifications.services import NotificationService


async def get_notification_service(
    session: AsyncSession = Depends(get_session)
) -> NotificationService:
    return NotificationService(session)
