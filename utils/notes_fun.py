import datetime
from flask import request, jsonify


import models.notes_model as note
# import utils.users_fun as user_fun
import utils.fun as fun


def add_notes():
    _json = request.json
    _title =_json["title"]
    _description = _json["description"]
    _status = _json["status"]
    _notes_by = fun.get_user_by_id(request.headers)["id"]
    
    _note = note.Notes(
    title=_title, 
    description = _description, 
    status = _status,
    notes_by = _notes_by
    )
    _note.save()
    resp = jsonify("Note added.")
    return resp

def update_note(id):
    _id = id
    _json = request.json
    _title = _json["title"]
    _description = _json["description"]

    selected_note = note.Notes.objects(id=_id)
    selected_note.update(
        set__title=_title,
        set__description=_description
    )
    resp = jsonify("note updated successfully.")
    resp.status_code = 200
    return resp    

def delete_note(id):
    _id = id

    selected_note = note.Notes._objects(id=_id)
    selected_note.delete()

def like_note(id):
    _id = id

    selected_note = note.Notes.objects.get(id=_id)
    
    like_count = selected_note["likes"]
    like_count = like_count + 1

    selected_note.update(
        set__likes = like_count
    )
    resp = jsonify("likes added successfully.")
    return resp

def comment_note(id):
    _id = id

    selected_note = note.Notes.objects.get(id=_id)

    _comments_stated = request.json["comments_stated"]
    _comments_by = request.json["comments_by"]
    _comments_date = datetime.datetime.utcnow()

    note.update(
        set__comments = {
            "comments_stated":_comments_stated,
            "comments_by":_comments_by,
            "comments_date":_comments_date
        }
    )

    resp = jsonify("Comments added.")
    return resp

def get_note(id):
        _id = id

        selected_note = note.Notes.objects.get(id=_id)
        return jsonify({
            "title" : selected_note["title"],
            "description" : selected_note["description"],
            "likes": selected_note["likes"],
            "comments": selected_note["comments"],
            "status": selected_note["status"],
            "created_at":selected_note["created_at"],
            "notes_by": selected_note["notes_by"]
        }
        )