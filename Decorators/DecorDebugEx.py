def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}\n")
        return result
    return wrapper
@debug
def multiply(a, b):
    return a * b
@debug
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
@debug
def add_numbers(*numbers):
    return sum(numbers)
multiply(3, 5)
greet("Harsha", greeting="Namaste")
add_numbers(1, 2, 3, 4, 5)
