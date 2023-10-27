from pydantic import BaseModel, Field

class UserBase(BaseModel):
    username: str
    name: str

class DeskBase(BaseModel):
    name: str
    owner: UserBase
