from app import db
from enum import Enum
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    COURIER = "courier"
    OFFICE_STAFF = "office_staff"


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'
    UserID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    Role = db.Column(db.Enum(Role), nullable=False)
    UserName = db.Column(db.String(255), nullable=False)
    UserPassword = db.Column(db.String(255), nullable=False)
    UserPhone = db.Column(db.String(255), nullable=True)
    UserAddress = db.Column(db.String(255), nullable=True)
    # OfficeID = db.Column(db.String(255), nullable=False)


class Shipment(db.Model):
    """
    快递表
    """
    __tablename__ = 'shipment'

    ShipmentID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    UserID = db.Column(db.Integer, nullable=False)
    ShipmentTime = db.Column(db.Date, nullable=False)
    SenderAddress = db.Column(db.String(255), nullable=False)
    ReceiverAddress = db.Column(db.String(255), nullable=False)
    CourierID = db.Column(db.Integer)
    Status = db.Column(db.String(255))


class Branch(db.Model):
    """
    网点表
    """
    __tablename__ = 'branch'

    BranchID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    BranchName = db.Column(db.String(255), nullable=False)
    BranchAddress = db.Column(db.String(255), nullable=False)


class Office(db.Model):
    """
    营业厅表
    """
    __tablename__ = 'office'

    OfficeID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    OfficeName = db.Column(db.String(255), nullable=False)
    OfficeAddress = db.Column(db.String(255), nullable=False)


class Task(db.Model):
    """
    收件送件任务表
    """
    __tablename__ = 'task'

    TaskID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    ShipmentID = db.Column(db.Integer, nullable=False)
    CourierID = db.Column(db.Integer, nullable=False)
    TaskType = db.Column(db.String(255), nullable=False)
    TaskStatus = db.Column(db.String(255), nullable=False)


class Complaint(db.Model):
    """
    投诉信息表
    """
    __tablename__ = 'complaint'

    ComplaintID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    UserID = db.Column(db.Integer, nullable=False)
    ComplaintTime = db.Column(db.Date, nullable=False)
    ComplaintContent = db.Column(db.Text, nullable=False)
    Status = db.Column(db.String(255), nullable=False)


if __name__ == "__main__":
    pass
