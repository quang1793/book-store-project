from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_ckeditor import CKEditor
app = Flask(__name__)
# Create Flask application
# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'

# Create in-memory database
app.config['DATABASE_FILE'] = 'Du_lieu/ql_ban_sach.sqlite'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
app.config['SQLALCHEMY_ECHO'] = False
db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='quang1234.py@gmail.com'
app.config['MAIL_PASSWORD']='Quang123'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

ckeditor=CKEditor(app)

#import ung_dung.Xu_ly.Xu_ly_Model
import ung_dung.Sach
import ung_dung.Gio_hang
import ung_dung.tin_tuc
import ung_dung.khach_hang
import ung_dung.do_thi