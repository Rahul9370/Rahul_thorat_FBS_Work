# WAP to check if given number is prime number or not using function recursion
def Prime(n, i=2):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return Prime(n, i + 1)

num = int(input("Enter number to check if it's prime: "))

if Prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")
