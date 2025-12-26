import enum


class NotificationType(str, enum.Enum):
    EMAIL = "EMAIL"


class NotificationStatus(str, enum.Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SENT = "SENT"
    FAILED = "FAILED"
