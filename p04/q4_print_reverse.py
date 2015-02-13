import sys
sys.setrecursionlimit(10000)
def reverse_int(n):
    if len(n) == 1:
        return n
    else:
        return n[-1]+reverse_int(n[:-1])
integer = input("Please enter an integer\n")
print(reverse_int(integer))
