from fastapi import APIRouter
from fastapi.params import Depends
from src.notifications.schemas import NotificationResponse, NotificationBase
from src.notifications.services import NotificationService
from src.dependencies import get_notification_service


router = APIRouter()


@router.post("/notifications", response_model=NotificationResponse)
async def create_new_notification(
        notification_data: NotificationBase,
        service: NotificationService = Depends(get_notification_service)
):
    result = await service.create_notification(notification_data)
    return result
