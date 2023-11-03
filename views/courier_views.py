import json

from flask import Blueprint, request, jsonify

from app import db
from database.models import User, Shipment
from utils.jwt_utils import require_role
from utils.log_utils import Logging

log = Logging().get_logger()
courier_view = Blueprint("courier_view", __name__)


@courier_view.route('/courier/register', methods=['POST'])
@require_role(role='courier')
def register():
    """
    快递登记
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    sender_name = data.get('sender_name')
    receiver_name = data.get('receiver_name')
    courier_name = data.get('courier_name')
    sender = User.query.filter_by(Role='user', UserName=sender_name).first()
    receiver = User.query.filter_by(Role='user', UserName=receiver_name).first()
    courier = User.query.filter_by(Role='courier', UserName=courier_name).first()
    status = '1'
    shipment = Shipment(SenderID=sender.UserID, ReceiverID=receiver.UserID, CourierID=courier.UserID, Status=status)
    shipment.add()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'register success'})


@courier_view.route('/shipment/info', methods=['GET', 'POST'])
@require_role(role='courier')
def shipment_info():
    """
    快递信息查询，已揽件，运输中，已签收，已退回
    :return:
    """
    pass


@courier_view.route('/shipment/modify', methods=['GET', 'POST'])
@require_role(role='courier')
def shipment_modify():
    """
    快递信息修改
    :return:
    """
    pass
