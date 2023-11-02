from flask import Blueprint

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
    pass


@courier_view.route('/courier/information', methods=['GET', 'POST'])
@require_role(role='courier')
def information():
    """
    信息查询
    :return:
    """
    pass


@courier_view.route('/courier/modify', methods=['GET', 'POST'])
@require_role(role='courier')
def modify():
    """
    信息修改
    :return:
    """
    pass
