n=int(12000**0.333+1)
while n**3>12000:
    n -= 1
print("The largest integer n such that n^3 is less than 12,000 is:", n)
