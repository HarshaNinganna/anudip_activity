dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = {}
for d in (dic1, dic2, dic3):
    merged_dict.update(d)
print("Merged Dictionary:", merged_dict)
