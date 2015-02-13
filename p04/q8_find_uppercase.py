import sys
sys.setrecursionlimit(10000)
def find_num_uppercase(str) :
    if len(str) == 0:
        return 0
    else:
        if str[0].isupper() == True:
            return 1+find_num_uppercase(str[1:])
        else:
            return 0+find_num_uppercase(str[1:])
string = input("Please enter an integer\n")
print(find_num_uppercase(string))
