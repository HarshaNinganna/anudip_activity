friend1 = input("Enter hobbies of Friend 1 (comma-separated): ")
friend2 = input("Enter hobbies of Friend 2 (comma-separated): ")
hobbies1 = set(h.strip().lower() for h in friend1.split(','))
hobbies2 = set(h.strip().lower() for h in friend2.split(','))
common = hobbies1 & hobbies2
all_hobbies = hobbies1 | hobbies2
unique_to_each = hobbies1 ^ hobbies2
print("\nCommon Hobbies:", common)
print("All Hobbies:", all_hobbies)
print("Unique Hobbies to Each Friend:", unique_to_each)
