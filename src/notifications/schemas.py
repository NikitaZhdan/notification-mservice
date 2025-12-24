from pydantic import BaseModel
from src.models.enums import NotificationStatus


class NotificationBase(BaseModel):
    type: str
    recipient: str
    payload: str
    idempotency_key: str


class NotificationResponse(BaseModel):
    recipient: str
    status: NotificationStatus
