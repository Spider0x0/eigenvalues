# Lib => sympy : unknown variable , matrix , solve , equation
from sympy import Matrix, symbols ,solve, Eq 

# Unknown Variable
x = symbols("x") 
# The Main Matrix
A = [
    [3,5],
    [-2,-4]
]
# Result Matrix 
result = [
    [0,0],
    [0,0]
]
# Unit Matrix
I = [
    [1,0],
    [0,1]
]
# Find :  A - XI
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] - x * I[i][j]

# Convert To Matrix
result = Matrix(result)

# Find The determinant

det = result.det()

# Equation 

equation = Eq(det, 0)

# Solve The Equation (det = 0)
solutions = solve(equation, x) # Solutions is List 

# Print The Solutions
print(solutions)
