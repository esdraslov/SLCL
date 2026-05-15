from flask import Flask, jsonify, request, render_template
import os
import json
import configparser

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("slcl.conf")

library_path = config["server"]["library_path"]
validade_hosts = bool(config["security"]["validade_hosts"])

@app.route("/")
def home():
    return "Starlight Custom Library python script running"

@app.route("/api/v3/mods")
def listmods():
    mods = []

    if validade_hosts:
        pass # TODO

    for folderfile in os.listdir(library_path):
        if os.path.isdir(os.path.join(library_path, folderfile)):
            with open(os.path.join(library_path, folderfile, "manifest.json"), "r") as manifest:
                info = json.load(manifest)
                info["_links"] = {
                    "self": request.url + f"/{folderfile}",
                    "thumbail": request.url + f"/{folderfile}/thumbnail",
                    "versions": request.url + f"/{folderfile}/versions"
                }
                info["id"] = folderfile
                mods.append(info)
                print("a")

    return jsonify(mods)

    # return jsonify([{
    #     "mod_type": "All Clients", # If the mod is host only, all clients or client only
    #     "id": "esdraslov.test.mod", # the mod unique identifier
    #     "name": "Testing mod", # Display name
    #     "author": "Esdraslov", # author
    #     "description": "Test description", # description
    #     "created_at": 0, # creation timestamp, probably unix epoch
    #     "updated_at": 0, # last update timestamp
    #     "downloads": 0, # how many downloads
    #     "_links": { # mostly useless links
    #         "self": "https://example.com", # USELESS, better cache this information
    #         "thumbnail": "https://example.com", # thumbnail
    #         "versions": "https://example.com" # link to versions download
    #     }
    # }])

@app.route("/api/v3/mods/<mod>")
def getmod(mod):
    if os.path.exists(os.path.join(library_path, mod)):
        with open(os.path.join(library_path, mod, "manifest.json"), "r") as manifest:
            info = json.load(manifest)
            info["_links"] = {
                "self": request.url,
                "thumbail": request.url + "/thumbnail",
                "versions": request.url + "/versions"
            }
            info["id"] = mod
            return jsonify(info)

@app.route("/api/v3/health")
def OK():
    return "OK"

@app.route("/browser")
def browser():
    return render_template("index.html")
