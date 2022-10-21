from fastapi import FastAPI
from database import database, updates
from models.update import UserUpdate, UserUpdateIn

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/update", response_model=UserUpdate)
async def create_update(update: UserUpdateIn):
    query = updates.insert().values(name=update.name, body=update.body)
    last_record_id = await database.execute(query)
    return {**update.dict(), "id": last_record_id}


@app.get("/updates", response_model=list[UserUpdate])
async def get_all_updates():
    query = updates.select()
    return await database.fetch_all(query)
