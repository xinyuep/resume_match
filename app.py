# app.py
import os
from flask import *           # import flask
import cosine
from flask_uploads import *
#from werkzeug.utils import secure_filename
#from werkzeug.middleware.shared_data import SharedDataMiddleware
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'I have a dream'
app.config['UPLOADED_DOCUMENTS_DEST'] = './'

documents = UploadSet('documents', ALL)
configure_uploads(app, documents)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    document = FileField(validators=[FileRequired()])
    submit = SubmitField(u'Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = UploadForm()
    if form.validate_on_submit():
        filename = documents.save(form.document.data)
        file_url = documents.url(filename)
        output = cosine.process(filename)
        return output
    else:
        file_url = None
    return render_template('index.html', form=form, file_url=file_url)

'''
@app.route("/")                   # at the end point /
def match():                      # call method hello
    return output                 # which returns top 3 matching job
'''

if __name__ == "__main__":        # on running python app.py
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0', port=port)                     # run the flask app
