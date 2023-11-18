def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
m = int(input("Enter the first integer: "))
n = int(input("Enter the second integer: "))
gcd = gcd(m, n)
print("The greatest common divisor of", m, "and", n, "is", gcd)