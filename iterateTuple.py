employee1 = ("Abhi", 1, "Human Resources", 60000)
employee2 = ("Harish", 2, "Marketing", 55000)
employee3 = ("Vijay", 3, "Engineering", 75000)
employees = [employee1, employee2, employee3]
print("Employee Records:")
for emp in employees:
    print(f"\nName: {emp[0]}")
    print(f"Employee ID: {emp[1]}")
    print(f"Department: {emp[2]}")
    print(f"Salary: {emp[3]}")
