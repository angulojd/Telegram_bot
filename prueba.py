from sympy import *
x = symbols('x')
init_printing(use_unicode=True)
v  = x**3 - 6*x**2 - 4*x + 8
a = solve(v)
b = factor_list(v)
c = factor(v)
if(c == v):
    print("VERDAD")
l = b[1]
print(a)
print(b)
print(c)
print("----------------------------------------------------")

for i in range(len(l)):
    print(l[i])
q = l[0]
for i in range(len(q)):
    print(q[i])
q = solve_linear(q[0])
print(q[1])


