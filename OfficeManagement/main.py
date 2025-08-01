from finance import Finance
from datetime import datetime
import random
import math

employee_id = random.randint(1000, 9999)
print(f"Employee ID: EMP{employee_id}")

emp_salary = 50000
emp_expense = 15000

fin = Finance(emp_salary, emp_expense)

print(f"Salary: ₹{emp_salary}")
print(f"Bonus (10%): ₹{fin.calculate_bonus()}")
print(f"Net Savings: ₹{fin.net_savings()}")

print("Payroll generated at:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
