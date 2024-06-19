# employees.py
from connector import Connector

class Employees:

    def get_all():
        query = "SELECT * FROM employees"

        Connector.cursor.execute(query)
        result = Connector.cursor.fetchall()
        
        return result
    
    def add_employee(emp_id, lname, fname, mname):
        query = "INSERT INTO employees VALUES (%s, %s, %s, %s)"

        try: 
            Connector.cursor.execute(query, (emp_id, lname, fname, mname))
            Connector.db.commit()
            print("ok")
            return True
        except:
            print("error")
            return False
    
    def get_employee(emp_id):
        query = "SELECT * FROM employees WHERE emp_id = %s"
        
        Connector.cursor.execute(query, (emp_id,))
        result = Connector.cursor.fetchone()
        
        return result

    def update_employee(emp_id, lname, fname, mname):
        query = "UPDATE employees SET lname = %s, fname = %s, mname = %s WHERE emp_id = %s"

        try:
            Connector.cursor.execute(query, (lname, fname, mname, emp_id))
            Connector.db.commit()
            return True
        except:
            return False

    def delete_employee(emp_id):
        query = "DELETE FROM employees WHERE emp_id = %s"

        try:
            Connector.cursor.execute(query, (emp_id,))
            Connector.db.commit()
            return True
        except:
            return False