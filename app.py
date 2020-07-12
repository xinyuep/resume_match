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
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,host='0.0.0.0', port=port)                     # run the flask app
