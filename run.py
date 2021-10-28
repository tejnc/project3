from api import app

from routes.notes_route import note_blueprint

app.register_blueprint(note_blueprint , url_prefix="/note")

if __name__ == "__main__":
    app.run(debug=True)