from flask import Blueprint ,request

import utils.notes_fun as note_fun


note_blueprint = Blueprint("notes",__name__)

@note_blueprint.route("/add",methods=["POST"])
def create_note():
    if request.method=="POST":
        return note_fun.add_notes()

@note_blueprint.route("/update",methods=["PUT"])
def update_note(id):
    return note_fun.update_note(id)

@note_blueprint.route("/delete/<id>",methods=["DELETE"])
def delete_note():
    if request.method=="DELETE":
        return note_fun.delete_note(id)

@note_blueprint.route("/like/<id>")
def like_note(id):
    return note_fun.like_note(id)

@note_blueprint.route("/comment/<id>",methods=["PUT"])
def comment_note(id):
    return note_fun.comment_note(id)

@note_blueprint.route("/get/<id>")
def get_note(id):
    return note_fun.get_note(id)