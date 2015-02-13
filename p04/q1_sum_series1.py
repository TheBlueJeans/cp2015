import sys
sys.setrecursionlimit(10000)
def sum_series1(i):
    if i == 1:
        return 1
    else:
        return 1/i+sum_series1(i-1)
integer = int(input("Enter a number\n"))
print(sum_series1(integer))
