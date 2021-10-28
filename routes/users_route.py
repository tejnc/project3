from flask import Blueprint, request, jsonify

import utils.users_fun as user_fun
import utils.fun as fun

user_blueprint = Blueprint("users",__name__)

@user_blueprint.route("/register",methods=["POST"])
def register_user():
    """"
        User registration
    """
    if request.method=="POST":
        return user_fun.register()

@user_blueprint.route("/login" , methods=["POST"])
def login_user():
    """
        User login
    """
    if request.method == "POST":
        return user_fun.login()

@user_blueprint.route("/update", methods=["PUT"])
def update_user():
    """
        update logged in user info
    """
    logged_email = fun.get_user_by_id(request.headers)["id"]
    return user_fun.update_user(logged_email)