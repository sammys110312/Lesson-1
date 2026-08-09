leaderboard = [
("Alice", 900),
("Bob", 870),
("Charlie", 820),
("David", 760),
("Emma", 700)
]

n = len(leaderboard)

for player in leaderboard:
    print(player[0], "-", player[1])

index = 2
player = leaderboard[index]
print("Player at Index", index, ":", player)
print("Complexity: O(1)")

target = "David"

step = 0
found = False

for player in leaderboard:
    step += 1
    
    if player[0] == target:
        found = True
        print("Found")
        break
if not found:
    print("Player not found")
print(step)

step = 0 

for i in range(n):
    for j in range(n):
        step += 1
        if leaderboard[i][1] > leaderboard[j][1]:
            pass
print("Nested pair comparison")
print(step)