import os
from flask import Flask, jsonify, render_template
from utils.log_utils import Logging
import sys
import traceback
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from common.base_exception import TopException

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = Logging().get_logger()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Xwj20021114.@localhost:3306/paedis?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['JSON_AS_ASCII'] = False
# login_manager = LoginManager()
# login_manager.init_app(app)
db = SQLAlchemy()
db.init_app(app)
CORS(app, supports_credentials=True)
from views.user_views import user_view
from views.auth_views import auth_view
from views.courier_views import courier_view
from views.office_views import office_view

app.register_blueprint(user_view, catch_all_except=True)
app.register_blueprint(auth_view, catch_all_except=True)
app.register_blueprint(courier_view, catch_all_except=True)
app.register_blueprint(office_view, catch_all_except=True)


# @app.errorhandler(Exception)
# def catch_all_except(e):
#     _, _, exc_traceback = sys.exc_info()
#     tb_list = traceback.extract_tb(exc_traceback)
#     method_name = tb_list[-1][2]
#     if isinstance(e, TopException):
#         log.error(f"{method_name} error, info is{e.msg}")
#         return jsonify({
#             "code": e.code,
#             "message": e.msg,
#             "data": None
#         })
#     else:
#         log.error(f"{method_name} error, info is {str(e)}")
#         log.error(f"{traceback.format_exc()}")
#         return jsonify({
#             "code": 500,
#             "message": None,
#             "data": str(e)
#         })


@app.cli.command()
def initdb():
    """
    初始化数据库
    :return:
    """
    from database.models import User, Shipment, Office, Task, Complaint
    try:
        db.drop_all()
        db.create_all()
        db.session.commit()
    except Exception as e:
        log.error(e)
        db.session.rollback()


@app.cli.command()
def init_admin():
    """
    初始化管理员
    :return:
    """
    from database.models import User
    admin = User(role='admin', username='admin', password='123456')
    db.session.add(admin)
    db.session.commit()


@app.cli.command()
def init_office():
    """
    初始化营业厅
    :return:
    """
    from database.models import Office
    office = Office(OfficeName='营业厅1', OfficeAddress='南京邮电大学')
    db.session.add(office)
    db.session.commit()


@app.route('/', methods=['GET'])
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
