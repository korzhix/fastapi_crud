from fastapi import FastAPI
from contact import routers

app = FastAPI(title='Contacts CRUD')
app.include_router(routers.contacts_router)
