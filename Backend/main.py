import re
from datetime import datetime
import os
from flask import Flask, make_response, request, url_for, send_from_directory, redirect
from uuid import uuid4
import json

app: Flask = Flask(__name__)
path: str = os.path
print(path)

save_path: str

@app.route("/")
def home():
    return send_from_directory(directory='static', path='index.html')

@app.route("/upload", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'GET':
        return send_from_directory(directory='static', path='upload.html')
    if request.method == 'POST' and request.files:
        files = request.files.getlist("file")
        print(files)

        for item in files:
            extension: str = item.filename.rsplit('.')[1]
            item.filename = str(uuid4()) + f".{extension}"
            save_path = os.path.join("file_store", item.filename)
            item.save(save_path)

        return redirect("/")

@app.get("/tree")
def get_tree():
    tree = os.walk(os.path.join("file_store"))
    tree = tree.__next__()
    return json.dumps(tree)


if __name__ == '__main__':
    app.run(debug=True, passthrough_errors=True)
