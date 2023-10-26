import datetime

# from redis_om import Field, EmbeddedJsonModel, JsonModel, Migrator, HashModel
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(16, unique=True)
    name = fields.CharField(32)
    date_join = fields.DateField(default=datetime.datetime.now)

UserPydantic = pydantic_model_creator(User, name='User')
UserInPydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

# class User(HashModel):
#     username: str = Field(index=True, full_text_search=True)
#     name: str
#    
#     date_join: datetime.date = Field(default=datetime.datetime.now())

#     class Meta:
#         database = redis


# class Project(HashModel):
#     user: User
    
#     class Meta:
#         database = redis

# class Project(Model)

# class Task(HashModel):
#     title: str
#     description: str
    
#     date: datetime.date = Field(default=datetime.datetime.now())
#     project: Project
    
#     class Meta:
#         database = redis
