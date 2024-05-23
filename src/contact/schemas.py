from pydantic import BaseModel
from pydantic import Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class Address(BaseModel):
    address_name: str = Field(examples=['Россия, республика Татарстан, город Казань, улица Братьев Касимовых, дом 64'],
                              max_length=256)


class Contact(BaseModel):
    phone: PhoneNumber = Field(examples=['+79090000000'])
    address: Address
