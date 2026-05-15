from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Starlight Custom Library python script running"

@app.route("/api/v3/mods")
def listmods():
    return jsonify([{
        "mod_type": "All Clients", # If the mod is host only, all clients or client only
        "id": "esdraslov.test.mod", # the mod unique identifier
        "name": "Testing mod", # Display name
        "author": "Esdraslov", # author
        "description": "Test description", # description
        "created_at": 0, # creation timestamp, probably unix epoch
        "updated_at": 0, # last update timestamp
        "downloads": 0, # how many downloads
        "_links": { # mostly useless links
            "self": "https://example.com", # USELESS, better cache this information
            "thumbnail": "https://example.com", # thumbnail
            "versions": "https://example.com" # link to versions download
        }
    }])
