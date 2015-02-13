import sys
sys.setrecursionlimit(10000)
def sum_series2(i):
    if i == 1:
        return 1/3
    else:
        return i/(i*2+1)+sum_series2(i-1)
integer = int(input("Enter a number\n"))
print(sum_series2(integer))
