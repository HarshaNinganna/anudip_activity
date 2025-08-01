class Reports:
    def generate_salary_slip(self, name, emp_id, salary, bonus, savings):
        slip = f"""
        ----------------------------
        Salary Slip - {name} (EMP{emp_id})
        ----------------------------
        Base Salary : ₹{salary}
        Bonus       : ₹{bonus}
        Savings     : ₹{savings}
        ----------------------------
        """
        return slip
