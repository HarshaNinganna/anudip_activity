def filter_strings(data):
    for item in data:
        if isinstance(item, str):
            yield item
mixed_data = [1, "hello", 3.14, "world", 42]
string_gen = filter_strings(mixed_data)
for s in string_gen:
    print(s)
