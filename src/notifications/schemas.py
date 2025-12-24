from pydantic import BaseModel
from uuid import UUID
from src.models.enums import NotificationStatus, NotificationType


class NotificationBase(BaseModel):
    type: NotificationType = NotificationType.EMAIL
    recipient: str
    payload: str
    idempotency_key: UUID


class NotificationResponse(BaseModel):
    recipient: str
    status: NotificationStatus
