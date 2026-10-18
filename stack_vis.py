def linear_recursion(n):
    if n == 0:
        return

    print("Linear call at level:", n)
    linear_recursion(n - 1)

linear_recursion(5)

def tail_recursion(n):
    if n == 0:
        return

    print("Tail work before call:", n)
    tail_recursion(n - 1)

tail_recursion(5)


def head_recursion(n):
    if n == 0:
        return

    head_recursion(n - 1)
    print("Head work after call:", n)

head_recursion(5)

def increasing_decreasing(n):
    if n == 0:
        return

    print("Going down:", n)
    increasing_decreasing(n - 1)
    print("Coming back:", n)


increasing_decreasing(5)

def tree_recursion(n):
    if n == 0:
        return

    print("Tree node:", n)
    tree_recursion(n - 1)
    tree_recursion(n - 1)

tree_recursion(3)