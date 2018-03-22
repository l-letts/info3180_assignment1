from flask import Flask
from flask_sqlalchemy import SQLAlchemy


SECRET_KEY = 'Sup3r$3cretkey'
UPLOAD_FOLDER = "./app/static/uploads"

app = Flask(__name__)
app.config['SECRET_KEY'] = "change this to be a more random key"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password@localhost/A1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)



app.config.from_object(__name__)
upload_f = app.config['UPLOAD_FOLDER']
Allowed_Uploads = ['jpg','png','jpeg']
app.debug= True
from app import views
