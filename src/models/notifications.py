import uuid
from datetime import datetime
from sqlalchemy import  Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from src.models.enums import NotificationType, NotificationStatus
from src.database.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True)

    idempotency_key: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    type: Mapped[NotificationType] = mapped_column(Enum(NotificationType), nullable=False)

    recipient: Mapped[str] = mapped_column(nullable=False)
    payload: Mapped[str] = mapped_column(nullable=False)

    status: Mapped[NotificationStatus] = mapped_column(Enum(NotificationStatus), default=NotificationStatus.PENDING)

    attempts: Mapped[int] = mapped_column(default=0)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
