import random
import math

def generate_employee_id():
    return f"EMP{random.randint(1000, 9999)}"

def calculate_tax(salary, tax_rate=5):
    return math.ceil(salary * (tax_rate / 100))
