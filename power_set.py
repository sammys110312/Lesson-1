items = ["A", "B", "C"]
n = len(items)
total_subset = 2 ** n
print("Total Subsets:", total_subset)
for mask in range(total_subset):
    subset= []
    for i in range(n):
        if (mask >> i) & 1:
            subset.append(items[i])
    print(subset)