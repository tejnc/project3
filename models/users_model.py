import os
import jwt
import datetime
from dotenv import load_dotenv
from flask import request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from flask_mongoengine import MongoEngine


db = MongoEngine()
load_dotenv()

class Users(db.Document):
    name = db.StringField(required=True)
    gender = db.StringField()
    phone_number=db.StringField()
    address=db.DictField()
    email = db.EmailField(required=True,unique=True)
    password = db.StringField(required=True)
    created = db.DateTimeField(default=datetime.datetime.utcnow)

