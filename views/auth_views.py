from flask import Blueprint, request, jsonify
import json
from utils.log_utils import Logging
from database.models import User, Role
from app import db
from utils.jwt_utils import create_token, verify_token, get_username, get_role, require_role

log = Logging().get_logger()
auth_view = Blueprint("auth_view", __name__)


@auth_view.route('/register', methods=['POST'])
def register():
    """
    用户注册
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    username = data.get('username')
    password = data.get('password')
    role = 'user'
    user = User.query.filter_by(Role=role, UserName=username).first()
    if user is not None:
        log.error('user exist')
        return jsonify({'code': 400, 'message': 'user exist'})
    user = User()
    user.Role = role
    user.UserName = username
    user.UserPassword = password
    user.UserAddress = data.get('address')
    user.UserPhone = data.get('phone')
    db.session.add(user)
    db.session.commit()
    return jsonify({'code': 200, 'message': 'register success'})


@auth_view.route('/login', methods=['POST'])
def login():
    data = json.loads(request.get_data().decode('utf-8'))
    role = data.get('role')
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(Role=role, UserName=username).first()
    if user is None:
        return jsonify({'code': 400, 'message': 'user not exist'})
    if user.UserPassword != password:
        return jsonify({'code': 400, 'message': 'password error'})
    token = create_token(role=role, username=username)
    return jsonify({'code': 200, 'message': 'login success', 'token': token})


@auth_view.route('/logout', methods=['GET', 'POST'])
def logout():
    pass


@require_role(role='user')
@auth_view.route('/user', methods=['GET', 'POST'])
def user():
    return jsonify({'code': 200, 'message': 'user authority  success'})


@require_role(role='admin')
@auth_view.route('/admin', methods=['GET', 'POST'])
def admin():
    return jsonify({'code': 200, 'message': 'admin authority success'})


@require_role(role='courier')
@auth_view.route('/courier', methods=['GET', 'POST'])
def courier():
    return jsonify({'code': 200, 'message': 'courier authority success'})
