# Direct access — O(1)
scores = [80, 75, 90, 85, 95]

print(scores[2])


# Linear search — O(n)
scores = [80, 75, 90, 85, 95]
wanted = 90

for score in scores:
    if score == wanted:
        print("Found!")

# Pair comparison — O(n²)
scores = [80, 75, 90, 85, 95]

for i in range(len(scores)):
    for j in range(len(scores)):
        if scores[i] == scores[j]:
            print("Same score")