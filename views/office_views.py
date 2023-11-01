from flask import Blueprint
from utils.log_utils import Logging

log = Logging().get_logger()
office_view = Blueprint("office_view", __name__)


@office_view.route('/office/modify', methods=['GET', 'POST'])
def modify():
    """
    网点信息修改
    :return:
    """
    pass


@office_view.route('/office/worker', methods=['GET', 'POST'])
def worker():
    """
    营业厅工作人员管理
    :return:
    """
    pass


@office_view.route('/office/courier', methods=['GET', 'POST'])
def courier():
    """
    快递员管理
    :return:
    """
    pass


@office_view.route('/office/task', methods=['GET', 'POST'])
def task():
    """
    收件送件任务指派
    :return:
    """
    pass


@office_view.route('/office/express', methods=['GET', 'POST'])
def express():
    """
    快递信息查询
    :return:
    """
    pass


@office_view.route('/office/complaint', methods=['GET', 'POST'])
def complaint():
    """
    投诉信息处理
    :return:
    """
    pass
