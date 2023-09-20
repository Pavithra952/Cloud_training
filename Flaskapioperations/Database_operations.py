import sqlite3

DATABASE = 'employee.db'

def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

def add_employee(name, department, salary):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", (name, department, salary))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False

def get_employee(employee_id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE id=?", (employee_id,))
        employee = cursor.fetchone()
        conn.close()

        if employee:
            return {
                'id': employee[0],
                'name': employee[1],
                'department': employee[2],
                'salary': employee[3]
            }
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None

def get_employees():
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()
        conn.close()

        employee_list = []
        for emp in employees:
            employee_list.append({
                'id': emp[0],
                'name': emp[1],
                'department': emp[2],
                'salary': emp[3]
            })
        return employee_list

    except Exception as e:
        print("Error:", e)
        return None

def update_employee(employee_id, name, department, salary):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE employees SET name=?, department=?, salary=? WHERE id=?", (name, department, salary, employee_id))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False

def delete_employee(employee_id):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE id=?", (employee_id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False
