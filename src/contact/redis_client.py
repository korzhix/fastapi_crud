import redis.asyncio as redis

from fastapi import Depends
from typing import Annotated
from src import config


async def get_redis_connection(settings: Annotated[config.Settings, Depends(config.get_settings)]) -> redis.Redis:
    pool = redis.ConnectionPool.from_url(settings.REDIS_URL)
    client = redis.Redis.from_pool(pool)
    yield client
    await client.close()
