# app.py
import os
from flask import Flask           # import flask
import cosine
app = Flask(__name__)             # create an app instance
#app.config.from_object(os.environ['APP_SETTINGS'])
output = cosine.process()

@app.route("/")                   # at the end point /
def match():                      # call method hello
    return output                 # which returns "hello world"

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True,host='127.0.0.1', port=5000)                     # run the flask app
