def stack_down(n):
    print("Current recursion level:", n)
    if n == 5:
        print("Base case reached")
        return
    stack_down(n + 1)

stack_down(1)
print("Program finished")