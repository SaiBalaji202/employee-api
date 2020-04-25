from flask_restful import Resource, request, reqparse
from models.employee import EmployeeModel
from datetime import datetime


class Employee(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="name is required")

    parser.add_argument('date',
                        type=str,
                        required=True,
                        help="date is required")

    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="status is required")

    def get(self, _id=None):
        if not _id:
            return {'message': 'Route Parameter _id is missing'}, 400
        employee = EmployeeModel.find_by_id(_id)
        if employee:
            return employee.json()
        return {'message': 'Employee not found'}, 404

    def post(self, _id=None):
        data = Employee.parser.parse_args()
        employee = EmployeeModel(**data)
        employee.date = datetime.strptime(employee.date, '%Y-%m-%d').date()
        try:
            employee.save()
        except:
            return {'message': 'An Error Occured while inserting'}, 500
        return employee.json(), 201

    def put(self, _id=None):
        if not _id:
            return {'message': 'Route Parameter _id is missing'}, 400

        data = Employee.parser.parse_args()
        employee = EmployeeModel.find_by_id(_id)

        if not employee:
            return {'message': 'Employee not found'}, 404

        if employee:
            employee.name = data['name']
            employee.status = data['status']
            employee.date = datetime.strptime(data['date'], '%Y-%m-%d').date()

        try:
            employee.save()
        except:
            return {'message': 'An Error Occured while updating'}, 500
        return employee.json()

    def delete(self, _id=None):
        if not _id:
            return {'message': 'Route Parameter _id is missing'}, 400

        employee = EmployeeModel.find_by_id(_id)
        if not employee:
            return {'message': 'Employee not found'}, 404

        try:
            employee.delete()
        except:
            return {'message': 'An Error Occured while deleting'}, 500
        return {'message': 'Employee Deleted'}


class EmployeeList(Resource):
    def get(self):
        query_params = dict(request.args)
        if query_params.get('name', None):
            data = EmployeeModel.query.filter(
                EmployeeModel.name.startswith(query_params["name"])).all()
        else:
            data = EmployeeModel.query.all()
        return {'employees': list(map(lambda employee: employee.json(), data))}


# ses.query(Table).filter(Table.fullFilePath.like('path%')).all()
# Model.query.filter(Model.columnName.contains('sub_string'))
