visitors = set()
n = int(input("How many visitors visited the website? "))
for i in range(n):
    name = input(f"Enter visitor {i + 1} name or ID: ").strip()
    visitors.add(name)
print("\nUnique Visitors:")
print(visitors)
print("Total number of unique visitors:", len(visitors))
