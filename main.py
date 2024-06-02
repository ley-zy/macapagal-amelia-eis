from flask import Flask, render_template, request, redirect, session
from users import Users
from employees import Employees

app = Flask(__name__)
app.secret_key = "gege"
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form["username"]
    password = request.form["password"]

    result = Users.check_user(username, password)

    if result:
        return redirect('/employee-list')
    else:
        return render_template('index.html')
    
@app.route('/employee-list')
def employee_list():
    employees = Employees.get_all()
  
    if "message" not in session:
        session["message"] = ""

    return render_template('employee_list.html', employees=employees, message=session.get('message'))

@app.route('/add-form')
def add_employees():
    return render_template('add_employee.html')

@app.route('/add-employee', methods=["POST"])
def add_employee():
    emp_id = request.form["emp_id"]
    lname = request.form["lname"]
    fname = request.form["fname"]
    mname = request.form["mname"]

    success = Employees.add_employee(emp_id, lname, fname, mname)

    if success:
        session["message"] = "Successfuly added"
    else:
        session["message"] = "Failed to add employee"

    return redirect('/employee-list')


if __name__ == '__main__':
    app.run()    
