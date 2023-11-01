from flask import Blueprint
from utils.log_utils import Logging

log = Logging().get_logger()
user_view = Blueprint("user_view", __name__)


@user_view.route('/user/register', methods=['POST'])
def register():
    pass


@user_view.route('/user/login', methods=['POST'])
def login():
    pass


@user_view.route('/user/logout', methods=['GET', 'POST'])
def logout():
    pass


@user_view.route('/protected', methods=['GET', 'POST'])
def protected():
    pass


@user_view.route('/user/send', methods=['GET', 'POST'])
def send():
    """
    寄件
    :return:
    """
    pass


@user_view.route('/user/branch', methods=['GET', 'POST'])
def branch():
    """
    网点查询
    :return:
    """
    pass


@user_view.route('/user/express', methods=['GET', 'POST'])
def express():
    """
    查快递
    :return:
    """
    pass


@user_view.route('/user/complaint', methods=['GET', 'POST'])
def complaint():
    """
    投诉反馈
    :return:
    """
    pass
