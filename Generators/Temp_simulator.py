def temperature_simulator():
    value = -10
    step = 4
    while True:
        value = ((value + step) % 46) - 10
        yield value
temp_gen = temperature_simulator()
for _ in range(5):
    temp = next(temp_gen)
    print(f"Temperature: {temp:.2f}°C")

