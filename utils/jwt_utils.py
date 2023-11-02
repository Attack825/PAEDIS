from functools import wraps

import jwt
import datetime

from flask import jsonify, request
from jwt import PyJWTError

from common.base_exception import RoleError
from utils.log_utils import Logging
from database.models import Role, User

log = Logging().get_logger()
JWT_SALT = '6jauHYese&N@48g7jphPJX6TyedLZ=@gvAY4mpnkgrgfmWhjdLKsYSNS@q@BaEWHqYHq*5T^*$c*HsL$r7K45JFEESP' \
           'cYfTGn&U!V=yM#54QsS^mPTV8c3=vw6ZB9rc@'
TIMEOUT = 1664


def create_token(role, username):
    """
    创建token
    :param role: 角色
    :param username: 用户名
    :return: token
    """
    role_list = [item.value for item in Role]
    if role not in role_list:
        log.error('role error')
        return False
    payload = {}
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(minutes=TIMEOUT)
    payload['role'] = role
    payload['username'] = username
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers)
    return result


def verify_token(token):
    """
    校验token是否合法
    :param token: token
    :return: bool
    """
    try:
        jwt.decode(token, JWT_SALT, algorithms=['HS256'])
        return True
    except PyJWTError as e:
        log.error(e)
        return False


def get_username(token):
    """
    校验token的正确性并返回username
    :param token: token
    :return: username
    """
    res = jwt.decode(token, JWT_SALT, algorithms=['HS256'])
    return res['username']


def get_role(token):
    """
    校验token的正确性并返回role
    :param token: token
    :return: role
    """
    res = jwt.decode(token, JWT_SALT, algorithms=['HS256'])
    return res['role']


def require_role(role):
    """
    权限认证装饰器，仅用在控制器层的装饰器，需要加在装饰器顺序的最前面
    example:
    @bp.route('/getUserInf', methods=['GET'])
    @require_role(role='user')
    def start_flask():

    :param role: 要和数据库匹配的权限字符
    :return: None
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token = request.headers.get('token')
            if token is None or not verify_token(token):
                log.error('token错误')
                raise RoleError('token error')
            if get_role(token) == 'admin':
                return func(*args, **kwargs)
            if get_role(token) != role:
                log.error('角色权限不足')
                raise RoleError('role error')
            return func(*args, **kwargs)

        return wrapper

    return decorator


if __name__ == '__main__':
    token = create_token('admin', 'admin')
    print(token)
    print(verify_token(token))
    print(get_username(token))
    print(get_role(token))
