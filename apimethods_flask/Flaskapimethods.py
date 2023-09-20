from flask import Flask, request, jsonify
from database_operations import create_table, add_employee, get_employees

app = Flask(__name__)

@app.route('/employees', methods=['POST'])
def create_employee():
    try:
        data = request.get_json()
        name = data['name']
        department = data['department']
        salary = data['salary']

        if add_employee(name, department, salary):
            return jsonify({"message": "Employee created successfully"}), 201
        else:
            return jsonify({"error": "Unable to create employee"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/employees', methods=['GET'])
def read_employees():
    employees = get_employees()

    if employees:
        return jsonify(employees)
    else:
        return jsonify({"message": "No employees found"}), 404

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
