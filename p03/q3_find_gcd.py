def gcd(m, n):
    for i in range(1, min(m, n)+1):
        if m%i == 0 and n%i == 0:
            gcd = i
    return gcd
int1 = int(input("Please enter an integer\n"))
int2 = int(input("Please enter another integer\n"))
print(gcd(int1, int2))
