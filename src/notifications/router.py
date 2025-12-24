from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.session import get_session
from src.notifications.schemas import NotificationResponse, NotificationBase
from src.notifications.services import NotificationService


router = APIRouter()


@router.post("/notifications")
async def create_new_notification(
        notification_data: NotificationBase,
        session: AsyncSession = Depends(get_session)
) -> NotificationResponse:

    service = NotificationService(session)
    result = await service.create_notification(notification_data)

    return result
