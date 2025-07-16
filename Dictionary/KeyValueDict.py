input_dict = {1: 10, 2: 20, 3: None, 4: 40, 5: None, 6: 60}
print("Keys:")
for key in input_dict.keys():
    print(key)
print("\nValues:")
for value in input_dict.values():
    print(value)
print("\nItems:")
for key, value in input_dict.items():
    print(f"Key: {key}, Value: {value}")
