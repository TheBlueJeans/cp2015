def prime(largest, primes=[2, 3, 5, 7, 11, 13]):
    num = 15
    while primes[-1] < largest:
        legit = True
        for prime in primes:
            if prime > num**0.5:
                break
            if num % prime == 0:
                legit = False
                break
        if legit == True:
            primes.append(num)
        num += 2
    return primes


def find_2_primes(even, p=[2, 3, 5, 7, 11, 13]):
    num = int(even/2)
    if num%2 == 1:
        num1 = num
        num2 = num
    else:
        num1 = num + 1
        num2 = num - 1
    p = prime(max(num1, num2), p)
    while not (num1 in p and num2 in p):
        num1 += 2
        num2 -= 2
        if (str(num1)[-1] == '5') or (str(num2)[-1] == '5'):
            num1 += 2
            num2 -= 2
        p = prime(max(num1, num2), p)
    return num1, num2, p

p = [2, 3, 5, 7, 11, 13]
while True:
    n = int(input("Enter even number above 3: \n"))
    num1, num2, p = find_2_primes(n, p)
    print(num1, num2)
    print()
