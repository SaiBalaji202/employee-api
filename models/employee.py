import sqlite3
from db import db


class EmployeeModel(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    date = db.Column(db.Date)
    status = db.Column(db.String(50))

    def __init__(self, name, status, date):
        self.name = name
        self.status = status
        self.date = date

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        return {'id': self.id, 'name': self.name, 'date': self.date.isoformat(), 'status': self.status}

    @classmethod
    def find_by_name(cls, name):
        return EmployeeModel.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return EmployeeModel.query.filter_by(id=_id).first()
