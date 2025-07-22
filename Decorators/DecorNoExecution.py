def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                print(f"Execution {i+1} of {times}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")
say_hello("Harsha")
