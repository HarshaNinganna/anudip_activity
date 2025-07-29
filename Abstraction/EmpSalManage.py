from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_employee_details(self):
        pass

    @abstractmethod
    def raise_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

    def get_employee_details(self):
        return f"Full-Time Employee: {self.name}, Monthly Salary: {self.monthly_salary}"

    def raise_salary(self):
        self.monthly_salary += 1000

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def get_employee_details(self):
        return f"Part-Time Employee: {self.name}, Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}"

    def raise_salary(self):
        self.hourly_rate += 10

full_time = FullTimeEmployee("Harsha", 50000)
part_time = PartTimeEmployee("Ashok", 500, 18)

print(full_time.get_employee_details())
print("Salary:", full_time.calculate_salary())
full_time.raise_salary()
print("After Raise Salary:", full_time.calculate_salary())

print()

print(part_time.get_employee_details())
print("Salary:", part_time.calculate_salary())
part_time.raise_salary()
print("After Raise Salary:", part_time.calculate_salary())
