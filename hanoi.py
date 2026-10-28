def hanoi(n, source, auxillary, destination):
    if n == 0 :
        return 0
    moves_before = hanoi(n-1, source, destination, auxillary)
    print(f"Move disk {n} from {source} to {destination}")
    current_move = 1
    moves_after = hanoi(n-1, auxillary, source, destination)
    return moves_after + moves_before + current_move
n = int(input("Enter number of disks- "))
if n < 0:
    print("Please enter zero or a positive integer.")
else:
    total_moves = hanoi(n, "A", "B", "C")
    print(total_moves)