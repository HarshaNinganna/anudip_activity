# Set --> A set is unordered, unindexed, and mutable collection of unique elements
Set1 = {11, 22, 33}
print("Set1:", Set1)

# Empty set must be created using set(), not ()
set2 = set()
print("Empty set2:", set2)

Birds = {"Crow", "Owl", "Peacock"}
print("Birds:", Birds)

print("----Adding Elements----")
Birds.add("Pigeon")
print("After adding Pigeon:", Birds)

print("----Removing Elements----")
Birds.remove("Peacock")  # will raise an error if not present
print("After removing Peacock:", Birds)

# discard vs remove
Birds.discard("Sparrow")  # no error even if Sparrow is not present
print("After discard 'Sparrow':", Birds)

# Using pop (removes a random element)
removed_bird = Birds.pop()
print(f"Popped element: {removed_bird}")
print("After pop:", Birds)

# Clear set
temp_set = {"a", "b", "c"}
temp_set.clear()
print("After clear():", temp_set)

# More set operations
set2 = {23, 45, 67}
print("----------Union---------")
a = {22, 45, 67, 89}
b = {34, 56, 78, 67, 56}  # duplicates will be removed automatically
print("Union of a and b:", a.union(b))

print("---------Intersection----------")
print("Intersection of a and b:", a.intersection(b))

print("---------Difference----------")
print("a - b:", a.difference(b))

print("---------Symmetric Difference----------")
print("Symmetric difference of a and b:", a.symmetric_difference(b))

# Practical use: Remove duplicates, fast membership testing, store unique unordered items

# Example: Student attendance
day1 = {"Anusha", "Prachi Kumari", "Uzma", "Chandrashekar C M"}
day2 = {"Anusha", "Prachi Kumari", "Manoj", "Govardhan"}

All = day1.union(day2)
print("All students:", All)

Present_Allday = day1.intersection(day2)
print("Present on both days:", Present_Allday)

print("----------Subset, Superset, Disjoint Check----------")
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("A is subset of B:", A.issubset(B))
print("B is superset of A:", B.issuperset(A))
print("A and B are disjoint:", A.isdisjoint({10, 20}))  # True if no common elements
