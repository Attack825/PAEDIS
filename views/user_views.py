from flask import Blueprint, request, jsonify
import json

from utils.jwt_utils import require_role, get_username
from utils.log_utils import Logging
from database.models import User, Shipment, Complaint, Office
from app import db
from datetime import datetime

log = Logging().get_logger()
user_view = Blueprint("user_view", __name__)


@user_view.route('/user/info', methods=['POST'])
@require_role(role='user')
def info():
    """
    用户信息查询
    :return:
    """
    username = get_username(request.headers.get('token'))
    user = User.query.filter_by(UserName=username).first()
    if user is None:
        return jsonify({'code': 400, 'message': 'user not exist'})
    return jsonify({
        'code': 200,
        'message': 'user query success',
        'data': {
            'user_id': user.UserID,
            'user_name': user.UserName,
            'user_address': user.UserAddress,
            'user_phone': user.UserPhone
        }
    })


@user_view.route('/user/send', methods=['POST'])
@require_role(role='user')
def send():
    """
    寄件
    需要参数：寄件人信息，收件人信息
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    log.info(data)
    sender_name = data.get('sender_name')
    receiver_name = data.get('receiver_name')
    sender = User.query.filter_by(Role='user', UserName=sender_name).first()
    receiver = User.query.filter_by(Role='user', UserName=receiver_name).first()
    shipment = Shipment(SenderID=sender.UserID, ReceiverID=receiver.UserID, ShipmentTime=datetime.now(),
                        Status='0')
    shipment.add()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'send success'})


@user_view.route('/user/office/info', methods=['GET', 'POST'])
@require_role(role='user')
def office_info():
    """
    网点查询,只产生一个网点
    :return:
    """
    office = Office.query.all()
    office_list = []
    for b in office:
        office_list.append({
            'branch_id': b.BranchID,
            'branch_name': b.BranchName,
            'branch_address': b.BranchAddress
        })
    return jsonify({'code': 200, 'message': 'office query success', 'data': office_list})


@user_view.route('/user/express', methods=['GET', 'POST'])
@require_role(role='user')
def express():
    """
    查自己的快递
    :return:
    """
    username = get_username(request.headers.get('token'))
    user_id = User.query.filter_by(UserName=username).first().UserID
    shipments = Shipment.query.filter_by(SenderID=user_id).all()
    shipment_list = []
    for s in shipments:
        shipment_list.append({
            'shipment_id': s.ShipmentID,
            'sender_id': s.SenderID,
            'receiver_id': s.ReceiverID,
            'shipment_time': s.ShipmentTime.strftime('%Y-%m-%d %H:%M:%S'),
            'courier_id': s.CourierID,
            'shipment_number': s.ShipmentNumber,
            'status': s.Status
        })
    return jsonify({'code': 200, 'message': 'express query success', 'data': shipment_list})


@user_view.route('/user/express/<shipment_number>', methods=['GET', 'POST'])
@require_role(role='user')
def express_detail(shipment_number):
    """
    根据快递单号查快递详情
    :param shipment_number: 快递单号
    :return:
    """
    shipment = Shipment.query.filter_by(ShipmentNumber=shipment_number).first()
    if shipment is None:
        return jsonify({'code': 400, 'message': 'shipment not exist'})
    return jsonify({
        'code': 200,
        'message': 'shipment query success',
        'data': {
            'shipment_id': shipment.ShipmentID,
            'sender_id': shipment.SenderID,
            'receiver_id': shipment.ReceiverID,
            'shipment_time': shipment.ShipmentTime.strftime('%Y-%m-%d %H:%M:%S'),
            'courier_id': shipment.CourierID,
            'shipment_number': shipment.ShipmentNumber,
            'status': shipment.Status
        }
    })


@user_view.route('/user/complaint', methods=['GET', 'POST'])
@require_role(role='user')
def complaint():
    """
    投诉反馈
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    username = get_username(request.headers.get('token'))
    complaint_content = data.get('complaint_content')
    complaint = Complaint(UserID=username, ComplaintContent=complaint_content, ComplaintTime=datetime.now(), Status='0')
    complaint.add()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'complaint success'})
