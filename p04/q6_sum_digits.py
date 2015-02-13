import sys
sys.setrecursionlimit(10000)
def sum_digits(n):
    if n//10 == 0:
        return n
    else:
        return n%10+sum_digits(n//10)
integer = int(input("Please enter an integer\n"))
print(sum_digits(integer))
