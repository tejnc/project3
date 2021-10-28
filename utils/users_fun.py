import os
import jwt
from flask import jsonify, request
from werkzeug.security import generate_password_hash,check_password_hash

import models.users_model as user

def register():
        _json = request.json
        _name = _json["name"]
        _gender = _json["gender"]
        _phone_number = _json["phone_number"]
        _address = {
            "province":_json["province"],
            "district":_json["district"],
            "town":_json["town"]
        }
        _email = _json["email"]
        _password = _json["password"]


        _hashed_password = generate_password_hash(_password)
        _user = user.Users(
            name=_name, 
            gender=_gender, 
            phone_number=_phone_number,
            address=_address,
            email=_email,
            password=_hashed_password)
        _user.save()
        resp = jsonify("User added successfully.")
        resp.status_code = 200
        return resp

def login():
    _json = request.json
    _email = _json["email"]
    _password = _json["password"]

    logged_user = user.Users.objects.get(email=_email)

    if _email == logged_user["email"] and check_password_hash(logged_user["password"], _password):
        token = jwt.encode(
            {
                "id": user["id"],
            },
            os.environ["KEY"]
    
        )


        return jsonify({
            "message": "User logged in successfully.",
            "token": token
        })
    
    else:
        return jsonify("Invalid email or password!")

def update_user(email):
    _email = email
    _json = request.json
    _name = _json["name"]
    _gender = _json["gender"]
    _phone_number = _json["phone_number"]

    logged_user = user.Users.objects(email=_email)
    logged_user.update(
        set__name = _name,
        set__gender = _gender,
        set__phone_number = _phone_number
    )

    return jsonify("user updated successfully.")