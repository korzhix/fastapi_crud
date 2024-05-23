from fastapi import APIRouter
from fastapi import Depends
from fastapi.exceptions import HTTPException

from redis.asyncio import Redis
from pydantic_extra_types.phone_numbers import PhoneNumber

from .schemas import Contact, Address
from .redis_client import get_redis_connection

contacts_router = APIRouter(tags=['Contacts'])


# Get phone as pk, look for it in db, create Address instance and response json shema
@contacts_router.get('/check_data', response_model=Address)
async def get_contact(phone: PhoneNumber, redis: Redis = Depends(get_redis_connection)):
    add_value = await redis.hget('contact', phone)
    if add_value is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return Address(address_name=add_value)


# put method does the same that hset. Create or update something by identifier
@contacts_router.put('/write_data/')
async def get_or_create_contact(contact: Contact, redis: Redis = Depends(get_redis_connection)):
    await redis.hset('contact', contact.phone, contact.address.address_name)
