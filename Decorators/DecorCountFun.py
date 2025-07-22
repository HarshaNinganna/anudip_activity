def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Function '{func.__name__}' has been called {wrapper.call_count} time(s).")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper
@count_calls
def greet(name):
    print(f"Hello, {name}!")
@count_calls
def add(a, b):
    return a + b
greet("Harsha")
greet("Dikshith")
add(3, 5)
add(10, 20)
add(1, 2)
