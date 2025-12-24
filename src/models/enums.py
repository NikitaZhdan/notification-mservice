import enum


class NotificationType(str, enum.Enum):
    EMAIl = "EMAIL"


class NotificationStatus(str, enum.Enum):
    PENDING = "PENDING"
    SENT = "SENT"
    FAILED = "FAILED"
