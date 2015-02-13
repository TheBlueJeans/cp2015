import sys
sys.setrecursionlimit(10000)
def find_largest(alist):
    if len(alist) == 1:
        return alist[0]
    else:
        if alist[-1]<alist[0]:
            return find_largest(alist[:-1])
        else:
            return find_largest(alist[1:])
integer = int(input("Please enter an integer for the length of the array\n"))
list = []
for i in range(1, integer+1):
    list.append(int(input("Please enter an integer for item {0}\n".format(i))))
print(find_largest(list))
