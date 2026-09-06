# Using a formula
laps = 5
points = 10

total = laps * points

print(total)

# Using a loop
laps = 5
points = 10
total = 0

for i in range(laps):
    total = total + points

print(total)

# Using a nested loop
laps = 5
points = 10
total = 0

for i in range(laps):
    for j in range(1):
        total = total + points

print(total)