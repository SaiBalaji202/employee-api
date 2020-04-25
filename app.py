from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.employee import Employee
from resources.employee import EmployeeList

from db import db

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

api = Api(app)

api.add_resource(Employee, '/employee', '/employee/<int:_id>')
api.add_resource(EmployeeList, '/employees')


@app.before_first_request
def create_table():
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
