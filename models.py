from __init__ import db


class Employees(db.Model):
    __table_args__ = {'schema': 'private'}
    __tablename__ = 'employees'

    empid = db.Column(db.String(100), primary_key=True, unique = True)
    empname = db.Column(db.String(100), unique = False)
    dateofbirth = db.Column(db.Date, unique = False)

    def __init__(self,empid,empname,dateofbirth):

        self.empid = empid
        self.empname = empname
        self.dateofbirth = dateofbirth

db.create_all()