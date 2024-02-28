# Prabhu Roka
# 1986444
def equation_sol(a1, b1, c1, a2, b2, c2):
    for x in range(-10, 11):
        for y in range(-10, 11):
            if (a1*x + b1*y == c1) and (a2*x + b2*y == c2):
                return x, y
    return None


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

solution = equation_sol(a, b, c, d, e, f)

if solution:
    print(*solution)
else:
    print("No solution")
