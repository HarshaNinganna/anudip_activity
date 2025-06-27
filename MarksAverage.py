
mark1 = float(input("Enter mark for subject 1: "))
mark2 = float(input("Enter mark for subject 2: "))
mark3 = float(input("Enter mark for subject 3: "))
mark4 = float(input("Enter mark for subject 4: "))
mark5 = float(input("Enter mark for subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Average Marks:", average)
print("Grade:", grade)
