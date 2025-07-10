employees = {
    101: {"name": "Bhoshan", "department": "HR", "salary": 50000},
    102: {"name": "prashanth", "department": "Engineering", "salary": 75000},
    103: {"name": "Smitha", "department": "Marketing", "salary": 60000}
}
try:
    emp_id = int(input("Enter Employee ID: "))
    if emp_id in employees:
        emp = employees[emp_id]
        print("\nEmployee Details:")
        print(f"Name       : {emp['name']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : ₹{emp['salary']}")
    else:
        print("Employee not found!")
except ValueError:
    print("Invalid input! Please enter a numeric employee ID.")
