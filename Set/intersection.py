set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
common = set1.intersection(set2)
if common:
    print("Common elements found:", common)
else:
    print("No common elements.")
