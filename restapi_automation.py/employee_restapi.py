import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


# Helper function to create the SQLite database and table
def create_employee_table():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Initialize the database
create_employee_table()


# API endpoints

# Create an employee
@app.route('/employees', methods=['POST'])
def create_employee():
    try:
        data = request.get_json()
        name = data['name']
        position = data['position']

        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO employees (name, position) VALUES (?, ?)', (name, position))
        conn.commit()
        conn.close()

        return jsonify({"message": "Employee created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Read all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    try:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employees')
        employees = cursor.fetchall()
        conn.close()

        employee_list = []
        for employee in employees:
            employee_data = {
                'id': employee[0],
                'name': employee[1],
                'position': employee[2]
            }
            employee_list.append(employee_data)

        return jsonify(employee_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Read a specific employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    try:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM employees WHERE id = ?', (id,))
        employee = cursor.fetchone()
        conn.close()

        if not employee:
            return jsonify({"message": "Employee not found"}), 404

        employee_data = {
            'id': employee[0],
            'name': employee[1],
            'position': employee[2]
        }
        return jsonify(employee_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Update an employee by ID
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    try:
        data = request.get_json()
        name = data['name']
        position = data['position']

        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE employees SET name = ?, position = ? WHERE id = ?', (name, position, id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Employee updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Delete an employee by ID
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        conn = sqlite3.connect('employee.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM employees WHERE id = ?', (id,))
        conn.commit()
        conn.close()

        return jsonify({"message": "Employee deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)
