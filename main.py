# main.py
from flask import Flask, render_template, request, redirect, session, url_for
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
    message = session.pop('message', "")
    return render_template('employee_list.html', employees=employees, message=message)

@app.route('/add-form')
def add_employees():
    return render_template('add_employee.html')

@app.route('/add-form', methods=["POST"])
def add_employee():
    emp_id = request.form["emp_id"]
    lname = request.form["lname"]
    fname = request.form["fname"]
    mname = request.form["mname"]

    success = Employees.add_employee(emp_id, lname, fname, mname)

    if success:
        session["message"] = "Employee successfully added"
    else:
        session["message"] = "Failed to add employee"
    
    return redirect('/employee-list')

@app.route('/update-employee/<emp_id>', methods=['GET', 'POST'])
def update_employee(emp_id):
    if request.method == 'POST':
        lname = request.form["lname"]
        fname = request.form["fname"]
        mname = request.form["mname"]

        success = Employees.update_employee(emp_id, lname, fname, mname)

        if success:
            session["message"] = "Employee successfully updated"
        else:
            session["message"] = "Failed to update employee"
        
        return redirect('/employee-list')
    else:
        employee = Employees.get_employee(emp_id)
        return render_template('update_employee.html', employee=employee)

@app.route('/delete-employee/<emp_id>')
def delete_employee(emp_id):
    success = Employees.delete_employee(emp_id)
    if success:
        session["message"] = "Employee successfully deleted"
    else:
        session["message"] = "Failed to delete employee"
    return redirect('/employee-list')

if __name__ == '__main__':
    app.run()
