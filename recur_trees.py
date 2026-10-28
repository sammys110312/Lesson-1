def paths(m, n):
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1
    right_paths = paths(m, n - 1)
    down_paths = paths(m - 1, n)
    return right_paths + down_paths
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
if rows <= 0 or columns <= 0:
    print("Rows and columns must be positive integers")
else:
    total_path = paths(rows, columns)
    print(total_path)