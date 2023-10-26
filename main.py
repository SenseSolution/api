import os

from fastapi import FastAPI

from database import User, UserPydantic, UserInPydantic
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI(title="todo api", version="0.0.2")

@app.on_event('startup')
async def startup():
    register_tortoise(
        app,
        db_url=str(os.getenv("DB_URL")),
        modules={'models': ['database.models']},
        generate_schemas=True
    )


@app.get("/")
async def main():
    return {"message", "Hello!"}

@app.post("/users")
async def create_user(user: UserInPydantic):
    obj = await User.create(**user.dict(exclude_unset=True))
    return await UserPydantic.from_tortoise_orm(obj)

@app.get("/users")
async def get_users():
    return await UserPydantic.from_queryset(User.all())

@app.get('users/{username}')
async def get_user(username: str):
    return await UserPydantic.from_queryset_single(User.get(username=username))
