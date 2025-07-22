def non_negative_integers_only(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, int) or arg < 0:
                return f"Invalid input: {arg}. Only non-negative integers are allowed."
        return func(*args, **kwargs)
    return wrapper
@non_negative_integers_only
def calculate_square_root(x):
    return x ** 0.5
print(calculate_square_root(9))   
print(calculate_square_root(-9)
