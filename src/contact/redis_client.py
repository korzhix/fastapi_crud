import redis.asyncio as redis

REDIS_URL = "redis://localhost"


async def get_redis_connection():
    pool = redis.ConnectionPool.from_url(REDIS_URL)
    client = redis.Redis.from_pool(pool)
    yield client
    await client.close()
