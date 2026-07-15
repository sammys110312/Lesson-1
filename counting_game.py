#Loops - 
def loops_solution(n):
    total = 0
    steps = 0
    for i in range(n):
        total += 10
        steps += 1
    return total,steps

#Formula -
def formula_solution(n):
    steps = 1
    total = n * 10
    return total,steps

#Recursion - 
def recursion_solution(n):
    if n == 0 :
        return 0,1
    total,steps = recursion_solution(n - 1)
    total += 10
    steps += 1
    return total,steps

print("Loops steps - Formula Steps - Recursion Steps - ")
for n in range(4,11):
    total1, step1 = loops_solution(n)
    total2, step2 = formula_solution(n)
    total3, step3 = recursion_solution(n)
    print(step1)
    print(step2)
    print(step3)