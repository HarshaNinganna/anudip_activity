def prime_number_generator():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1
gen = prime_number_generator()
for _ in range(15):
    print(next(gen), end=' ')
