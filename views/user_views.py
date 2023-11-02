from flask import Blueprint, request, jsonify
import json
from utils.log_utils import Logging
from database.models import User, Shipment, Branch, Office
from app import db

log = Logging().get_logger()
user_view = Blueprint("user_view", __name__)


@user_view.route('/user/send', methods=['POST'])
def send():
    """
    寄件
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    log.info(data)
    sender_name = data.get('sender_name')
    sender_phone = data.get('sender_phone')
    sender_address = data.get('sender_address')
    receiver_name = data.get('receiver_name')
    receiver_phone = data.get('receiver_phone')
    receiver_address = data.get('receiver_address')

    shipment = Shipment()
    shipment.add()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'send success'})


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
