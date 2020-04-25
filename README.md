# Flask REST API - Employees CRUD

I used pipenv to manage dependencies of this project.

## Install pipenv for Dependency Management
```
python -m pip install pipenv
```

## Install Dependencies
```
pipenv install
```

## Activate Virtual Environment
```
pipenv shell
```

## Running the code
```
python app.py
```

## Exiting the Virtual Environment
```
exit
```

## Available Routes
1) GET - http://localhost:5000/employees/
2) GET - http://localhost:5000/employees?name=<name>
3) GET - http://localhost:5000/employee/<employee_id>
4) POST - http://localhost:5000/employee
Header
```
{
'Content-Type': 'application/json'
}
```
Body
```
{
	"name": "abcd", 
	"status": "inactive", 
	"date": "2020-04-22"
}
```
5) PUT - http://localhost:5000/employee/<employee_id>
Header
```
{
'Content-Type': 'application/json'
}
```
Body
```
{
	"name": "abcd", 
	"status": "active", 
	"date": "2020-04-21"
}
```
6) DELETE - http://localhost:5000/employee/<employee_id>
