import json

from flask import Blueprint, jsonify, request

from app import db
from database.models import Complaint, Office, User, Shipment, Task
from utils.jwt_utils import require_role
from utils.log_utils import Logging

log = Logging().get_logger()
office_view = Blueprint("office_view", __name__)


@office_view.route('/office/info', methods=['GET', 'POST'])
@require_role(role='office_staff')
def office_info():
    """
    网点信息查询
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    office_id = data.get('office_id')
    office = Office.query.filter_by(OfficeID=office_id).first()
    if office is None:
        return jsonify({'code': 400, 'message': 'office not exist'})
    return jsonify({
        'code': 200,
        'message': 'office query success',
        'data': {
            'office_id': office.OfficeID,
            'office_name': office.OfficeName,
            'office_address': office.OfficeAddress
        }
    })


@office_view.route('/office/modify', methods=['GET', 'POST'])
@require_role(role='office_staff')
def office_modify():
    """
    网点信息修改
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    office_name = data.get('office_name')
    office_address = data.get('office_address')
    Office.query.filter_by(OfficeName=office_name).update({'OfficeAddress': office_address})
    db.session.commit()
    return jsonify({'code': 200, 'message': 'office modify success'})


@office_view.route('/office/worker/info', methods=['GET', 'POST'])
@require_role(role='office_staff')
def office_worker_info():
    """
    营业厅工作人员信息查询
    :return:
    """
    user = User.query.filter_by(Role='office_staff').all()
    if user is None:
        return jsonify({'code': 400, 'message': 'user not exist'})
    data = []
    for i in user:
        data.append({
            'user_id': i.UserID,
            'user_name': i.UserName,
            'user_address': i.UserAddress,
            'user_phone': i.UserPhone,
            'office_id': i.OfficeID
        })
    return jsonify({'code': 200, 'message': 'user query success', 'data': data})


@office_view.route('/office/worker/add', methods=['GET', 'POST'])
@require_role(role='admin')
def worker_add():
    """
    添加营业厅工作人员
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    user_name = data.get('user_name')
    user_password = data.get('user_password')
    user_phone = data.get('user_phone')
    user_address = data.get('user_address')
    office_id = data.get('office_id')
    user = User(UserName=user_name, UserPassword=user_password, UserPhone=user_phone, UserAddress=user_address,
                OfficeID=office_id)
    user.add()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'user add success'})


@office_view.route('/office/worker/delete', methods=['GET', 'POST'])
@require_role(role='admin')
def worker_delete():
    """
    删除营业厅工作人员
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    user_name = data.get('user_name')
    user = User.query.filter_by(UserName=user_name).first()
    if user is None:
        return jsonify({'code': 400, 'message': 'user not exist'})
    user.delete()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'user delete success'})


@office_view.route('/office/worker/modify', methods=['GET', 'POST'])
@require_role(role='admin')
def worker_modify():
    """
    修改营业厅工作人员信息
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    user_name = data.get('user_name')
    user_password = data.get('user_password')
    user_phone = data.get('user_phone')
    user_address = data.get('user_address')
    office_id = data.get('office_id')
    User.query.filter_by(UserName=user_name).update(
        {'UserPassword': user_password, 'UserPhone': user_phone, 'UserAddress': user_address, 'OfficeID': office_id})
    db.session.commit()
    return jsonify({'code': 200, 'message': 'user modify success'})


@office_view.route('/office/courier/info', methods=['GET', 'POST'])
@require_role(role='office_staff')
def courier_info():
    """
    快递员信息查询
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    office_id = data.get('office_id')
    user = User.query.filter_by(Role='courier', OfficeID=office_id).all()
    if user is None:
        return jsonify({'code': 400, 'message': 'user not exist'})
    data = []
    for i in user:
        data.append({
            'user_id': i.UserID,
            'user_name': i.UserName,
            'user_address': i.UserAddress,
            'user_phone': i.UserPhone,
            'office_id': i.OfficeID
        })
    return jsonify({'code': 200, 'message': 'courier query success', 'data': data})


@office_view.route('/office/courier/add', methods=['GET', 'POST'])
@require_role(role='office_staff')
def courier_add():
    """
    快递员信息添加
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    user_name = data.get('user_name')
    user_password = data.get('user_password')
    user_phone = data.get('user_phone')
    user_address = data.get('user_address')
    office_id = data.get('office_id')
    user = User(UserName=user_name, UserPassword=user_password, UserPhone=user_phone, UserAddress=user_address,
                OfficeID=office_id)
    user.add()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'courier add success'})


@office_view.route('/office/courier/delete', methods=['GET', 'POST'])
@require_role(role='office_staff')
def courier_delete():
    """
    快递员信息删除
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    user_name = data.get('user_name')
    user = User.query.filter_by(UserName=user_name).first()
    if user is None:
        return jsonify({'code': 400, 'message': 'user not exist'})
    user.delete()
    db.session.commit()
    return jsonify({'code': 200, 'message': 'courier delete success'})


@office_view.route('/office/courier/modify', methods=['GET', 'POST'])
@require_role(role='office_staff')
def courier_modify():
    """
    快递员信息修改
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    user_name = data.get('user_name')
    user_password = data.get('user_password')
    user_phone = data.get('user_phone')
    user_address = data.get('user_address')
    office_id = data.get('office_id')
    User.query.filter_by(UserName=user_name).update(
        {'UserPassword': user_password, 'UserPhone': user_phone, 'UserAddress': user_address, 'OfficeID': office_id})
    db.session.commit()
    return jsonify({'code': 200, 'message': 'courier modify success'})


@office_view.route('/office/task', methods=['GET', 'POST'])
@require_role(role='office_staff')
def task():
    """
    收件送件任务指派
    :return:
    """
    data = json.loads(request.get_data().decode('utf-8'))
    shipment_number = data.get('shipment_number')
    shipment = Shipment.query.filter_by(ShipmentNumber=shipment_number).first()
    courier_name = data.get('courier_name')
    task = Task(ShipmentID=shipment.ShipmentID, CourierID=courier_name, TaskStaus='0')
    task.add()
    db.session.commit()
    shipment.query.filter_by(ShipmentNumber=shipment_number).update({'Status': '1'})
    return jsonify({'code': 200, 'message': 'task add success'})


@office_view.route('/shipment/express', methods=['GET', 'POST'])
@require_role(role='office_staff')
def shipment_express():
    """
    快递信息查询
    :return:
    """
    shipment = Shipment.query.all()
    if shipment is None:
        return jsonify({'code': 400, 'message': 'shipment not exist'})
    data = []
    for i in shipment:
        data.append({
            'shipment_id': i.ShipmentID,
            'sender_id': i.SenderID,
            'receiver_id': i.ReceiverID,
            'shipment_time': i.ShipmentTime,
            'courier_id': i.CourierID,
            'shipment_number': i.ShipmentNumber,
            'status': i.Status
        })
    return jsonify({'code': 200, 'message': 'shipment query success', 'data': data})


@office_view.route('/office/complaint', methods=['GET', 'POST'])
@require_role(role='office_staff')
def complaint():
    """
    投诉信息处理
    :return:
    """
    data = request.get_data().decode('utf-8')
    complaint_id = data.get('complaint_id')
    Complaint.query.filter_by(ComplaintID=complaint_id, Status='0').update({'Status': '1'})
    complaint_result = '投诉已处理'
    db.session.commit()
    return jsonify({'code': 200, 'message': 'complaint success', 'data': complaint_result})
