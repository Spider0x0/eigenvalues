from sympy import Matrix, symbols ,solve, Eq ,N 


x = symbols("x") 


A = [
    [3,5],
    [-2,-4]
]
result = [
    [0,0],
    [0,0]
]
I = [
    [1,0],
    [0,1]
]


# Find :  A - XI
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - x * I[i][j]
 
result = Matrix(result)

det = result.det()

equation = Eq(det, 0)

solutions = solve(equation, x) # Solutions is List 

print(solutions)
