# app.py
from flask import Flask, render_template, request
import os
# import mysql.connector
from werkzeug import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

@app.route("/<name>")              # at the end point /<name>
def hello_name(name):              # call method hello_name
    return "Hello "+ name          # which returns "hello + name
	
@app.route('/upload')
def upload_file():
    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
	    f=request.files['file']
	    person=request.form['person']
	    p=os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))
	    f.save(p)
    with open(p) as s:
            file_content=s.read()
   # return 'file uploaded successfully'
    return "Uploaded By: "+person.upper()+" ::  "+file_content
		
	  

if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
