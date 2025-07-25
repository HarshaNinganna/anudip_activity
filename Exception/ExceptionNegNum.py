class NegativeNumberError(Exception):
    pass
def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    else:
        print("You entered:", num)
try:
    number = int(input("Enter a number: "))
    check_number(number)
except NegativeNumberError as e:
    print("Error:", e)
except ValueError:
    print("Please enter a valid number.")
