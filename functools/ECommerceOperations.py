from functools import reduce

products = [
    ("Laptop", 75000, "Electronics", True),
    ("Mouse", 700, "Electronics", True),
    ("T-Shirt", 1200, "Clothing", True),
    ("Jeans", 2500, "Clothing", False),
    ("Book", 350, "Books", True),
    ("Smartphone", 58000, "Electronics", False),
    ("Headphones", 2500, "Electronics", True),
]

discounted_products = list(map(lambda p: (p[0], round(p[1]*0.9), p[2], p[3]), products))
print(" Discounted Products:")
for p in discounted_products:
    print(f"  - {p[0]}: {p[1]} ({p[2]}) | In Stock: {p[3]}")

print("\n Products in stock over 1000 (filtered):")
filtered_products = list(filter(lambda p: p[1] > 1000 and p[3], discounted_products))
for p in filtered_products:
    print(f"  - {p[0]}: {p[1]}")

in_stock_prices = list(map(lambda p: p[1], filter(lambda p: p[3], discounted_products)))
total_revenue = reduce(lambda x, y: x + y, in_stock_prices)
print(f"\n Total potential revenue (from in-stock products): {total_revenue}")

electronics = list(filter(lambda p: p[2] == "Electronics", discounted_products))
all_electronics_in_stock = all([p[3] for p in electronics])
print(f"\n All electronics in stock? {'Yes' if all_electronics_in_stock else ' No'}")

sorted_products = sorted(discounted_products, key=lambda p: p[1])
print("\n Products sorted by discounted price:")
for i, p in enumerate(sorted_products, 1):
    print(f"  {i}. {p[0]} - {p[1]}")

featured = ["" if p[1] > 5000 else "" for p in discounted_products]
featured_list = list(zip(featured, [p[0] for p in discounted_products]))
print("\n Featured Products:")
for tag, name in featured_list:
    print(f"  {tag} {name}")
