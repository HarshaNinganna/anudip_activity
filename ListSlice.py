original_list = [1, 1, 2, 3, 4, 4, 5, 1]
split_index = int(input("Enter split index: "))

first_part = original_list[:split_index]
second_part = original_list[split_index:]

print("Original list:")
print(original_list)
print("Length of the first part of the list:", split_index)
print("Splitted the said list into two parts:")
print((first_part, second_part))

