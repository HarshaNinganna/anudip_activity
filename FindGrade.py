def find_grade(marks):
    avg=sum(marks)/len(marks)
    if avg>=90:
        return "A"
    elif avg>=80:
        return "B"
    elif avg>=70:
        return "C"
    else:
        return "Fail"
print("Grade:",find_grade((60,70,75,90)))
