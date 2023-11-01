from app import db


class User(db.Model):
    """
    用户表
    """
    __tablename__ = 'user'
    UserID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    UserName = db.Column(db.String(255), nullable=False)
    UserPhone = db.Column(db.String(255), nullable=False)
    UserPassword = db.Column(db.String(255), nullable=False)
    UserAddress = db.Column(db.String(255), nullable=False)


class Shipment(db.Model):
    """
    快递表
    """
    __tablename__ = 'shipment'

    ShipmentID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
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

    BranchID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    BranchName = db.Column(db.String(255), nullable=False)
    BranchAddress = db.Column(db.String(255), nullable=False)


class Courier(db.Model):
    """
    快递员表
    """
    __tablename__ = 'courier'

    CourierID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    CourierName = db.Column(db.String(255), nullable=False)
    CourierPhone = db.Column(db.String(255), nullable=False)
    CourierPassword = db.Column(db.String(255), nullable=False)


class Office(db.Model):
    """
    营业厅表
    """
    __tablename__ = 'office'

    OfficeID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    OfficeName = db.Column(db.String(255), nullable=False)
    OfficeAddress = db.Column(db.String(255), nullable=False)


class OfficeStaff(db.Model):
    """
    营业厅工作人员表
    """
    __tablename__ = 'office_staff'

    StaffID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    StaffName = db.Column(db.String(255), nullable=False)
    StaffPhone = db.Column(db.String(255), nullable=False)
    OfficeID = db.Column(db.Integer, nullable=False)
    StaffPassword = db.Column(db.String(255), nullable=False)


class Admin(db.Model):
    """
    系统管理员
    """
    __tablename__ = 'admin'
    AdminID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    AdminName = db.Column(db.String(255), nullable=False)
    AdminPhone = db.Column(db.String(255), nullable=False)
    AdminPassword = db.Column(db.String(255), nullable=False)


class Task(db.Model):
    """
    收件送件任务表
    """
    __tablename__ = 'task'

    TaskID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    ShipmentID = db.Column(db.Integer, nullable=False)
    CourierID = db.Column(db.Integer, nullable=False)
    TaskType = db.Column(db.String(255), nullable=False)
    TaskStatus = db.Column(db.String(255), nullable=False)


class Complaint(db.Model):
    """
    投诉信息表
    """
    __tablename__ = 'complaint'

    ComplaintID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    UserID = db.Column(db.Integer, nullable=False)
    ComplaintTime = db.Column(db.Date, nullable=False)
    ComplaintContent = db.Column(db.Text, nullable=False)
    Status = db.Column(db.String(255), nullable=False)
