def stair_way(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    one_step = stair_way(n - 1)
    two_step = stair_way(n - 2)
    return one_step + two_step
stairs = int(input("Enter the number of stairs"))
ways = stair_way(stairs)
print("Number of ways:", ways)