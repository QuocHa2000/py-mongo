from pymodm import connect, fields, MongoModel, EmbeddedMongoModel
from config.index import config


def initMongo():
    try:
        mongoUrl = "mongodb://" + \
            config['mongo']['host']+":"+config["mongo"]["port"]
        connect("mongodb://")
    except Exception as e:
        print("Getting error when init db", e)
        pass
