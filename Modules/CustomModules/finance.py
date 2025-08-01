class Shop:
    def __init__(self, expense, income):
        self.expense = expense
        self.income = income
        self.savings = income - expense

    def get_expense(self):
        return f"Expense: {self.expense}"

    def get_income(self):
        return f"Income: {self.income}"

    def get_savings(self):
        return f"Savings: {self.savings}" 

