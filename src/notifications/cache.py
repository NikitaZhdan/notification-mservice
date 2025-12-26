from redis.asyncio import Redis
from uuid import UUID


def _idem_key(idempotency_key: UUID) -> str:
    return f"notification:{idempotency_key}"


class NotificationCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    async def set_idem_key(self, ntf_id: int, idempotency_key: UUID, ttl: int) -> None:
        key = _idem_key(idempotency_key)
        await self.redis.set(key, ntf_id ,ex=ttl)


    async def get_idem_key(self, idempotency_key: UUID) -> str | None:
        key = _idem_key(idempotency_key)
        return await self.redis.get(key)
