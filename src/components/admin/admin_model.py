from pymongo.operations import IndexModel
from pymongo import TEXT
from pymodm import connect, fields, MongoModel, EmbeddedMongoModel


class AdminModel(MongoModel):
    email = fields.EmailField()
    name = fields.CharField()
