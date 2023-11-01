import os
from flask import Flask, jsonify, render_template
from utils.log_utils import Logging
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = Logging().get_logger()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/express?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['JSON_AS_ASCII'] = False
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
CORS(app, supports_credentials=True)


@app.route('/')
def index():
    return "hello world"


@app.cli.command()
def initdb():
    """
    初始化数据库
    :return:
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


@app.cli.command()
def init_admin():
    """
    初始化管理员
    :return:
    """
    from database.models import OfficeStaff
    admin = OfficeStaff(StaffName='admin', StaffPhone='123456')
    db.session.add(admin)
    db.session.commit()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
