class Finance:
    def __init__(self, base_salary, expenses):
        self.base_salary = base_salary
        self.expenses = expenses
        self.income = base_salary

    def calculate_bonus(self, percentage=10):
        return self.base_salary * (percentage / 100)

    def net_savings(self):
        return self.income - self.expenses
