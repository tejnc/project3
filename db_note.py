import os
from flask_mongoengine import MongoEngine

from api import app


app.config["MONGODB_SETTINGS"] = {
    'db':'notes_db',
    'host':os.environ["MONGO_URI"]
}

db = MongoEngine()
db.init_app(app)

