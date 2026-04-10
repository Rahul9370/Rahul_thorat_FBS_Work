# Program to find the Roots of a Quadratic Equation

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:"))

ans = (b*b) - (4*a*c)

ans = ans ** 0.5

root1 = (-b+ans) / 2*a
root2 = (-b-ans) / 2*a

print("Root 1 ans is(+):", root1)
print("Root 1 ans is(-):", root2)