import re
from datetime import datetime
import os
from flask import Flask, make_response, request, url_for
from uuid import uuid5 as idtool

app = Flask(__name__)


@app.route("/upload", method='POST')
def upload_file():
    request.files()
    response = make_response("<h1>Success</h1>")
    response.status_code = 200
    return response



if __name__ == '__main__':
    app.run(debug=True, passthrough_errors=True)
