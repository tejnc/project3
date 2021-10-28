import datetime
from flask import request,jsonify
from flask_mongoengine import MongoEngine

import db_note
import models.users_model as user
db = db_note.db

#TODO: create note - done
#TODO: update note  - partially done
#TODO: delete note - done
#TODO: like note   - done
#TODO: comment note - done
#TODO: get note  - done
#TODO: list notes 


class Notes(db.Document):
    title = db.StringField()
    description = db.StringField()
    likes=db.IntField(default=0)
    comments=db.DictField(required=False)
    status=db.StringField()
    created_at=db.DateTimeField(default=datetime.datetime.utcnow)
    notes_by=db.StringField()
    # updated_at=db.DateTimeField()


   