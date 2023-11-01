# from marshmallow import Schema, fields
#
#
# class UserSchema(Schema):
#     id = fields.Int()
#     username = fields.Str()
#     phone = fields.Str()
#     password = fields.Str()
#     address = fields.Str()
#     created_at = fields.DateTime()
#     updated_at = fields.DateTime()
#
#
# class ShipmentSchema(Schema):
#     id = fields.Int()
#     UserID = fields.Int()
#     ShipmentTime = fields.Date()
#     SenderAddress = fields.Str()
#     ReceiverAddress = fields.Str()
#     CourierID = fields.Int()
#     Status = fields.Str()
#
#
# class BranchSchema(Schema):
#     id = fields.Int()
#     BranchName = fields.Str()
#     BranchAddress = fields.Str()
#
#
# class CourierSchema(Schema):
#     id = fields.Int()
#     CourierName = fields.Str()
#     CourierPhone = fields.Str()
#
#
# class OfficeSchema(Schema):
#     id = fields.Int()
#     OfficeName = fields.Str()
#     OfficeAddress = fields.Str()
#
#
# class OfficeStaffSchema(Schema):
#     id = fields.Int()
#     StaffName = fields.Str()
#     StaffPhone = fields.Str()
#     OfficeID = fields.Int()
#
#
# class TaskSchema(Schema):
#     id = fields.Int()
#     ShipmentID = fields.Int()
#     CourierID = fields.Int()
#     TaskType = fields.Str()
#     TaskStatus = fields.Str()
#
#
# class ComplaintSchema(Schema):
#     id = fields.Int()
#     UserID = fields.Int()
#     ComplaintTime = fields.Date()
#     ComplaintContent = fields.Str()
#     Status = fields.Str()
