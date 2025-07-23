def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
def sum_fibonacci(n):
    gen = fibonacci_generator()
    total = 0
    for _ in range(n):
        total += next(gen)
    return total
print("Sum of first 10 Fibonacci numbers:", sum_fibonacci(10)
