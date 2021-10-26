from re import M
import notes

import os
import datetime
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine


app = Flask(__name__)
load_dotenv()

app.config["MONGODB_SETTINGS"] = {
    'db':'notes_db',
    'host':os.environ["MONGO_URI"]
}
db=MongoEngine()
db.init_app(app)

class Notes(db.Document):
    title = db.StringField()
    description = db.StringField()
    likes=db.BooleanField(default=False)
    comments=db.DictField()
    status=db.StringField()
    created_at=db.DateTimeField(default=datetime.datetime.utcnow)
    # updated_at=db.DateTimeField()


#TODO: create note 
#TODO: update note
#TODO: delete note
#TODO: like note
#TODO: comment note
#TODO: get note
#TODO: list notes

@app.route("/add",methods=["POST"])
def add_notes():
    _json = request.json
    _title=_json["title"]
    _description = _json["description"]
    _likes = _json["likes"]
    _comments = {
        "comments_by_user" : _json["comments_by_user"],
        "comments_date": _json["comments_date"]
    }
    


if __name__=="__main__":
    app.run(debug=True)