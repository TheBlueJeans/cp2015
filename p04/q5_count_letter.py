import sys
sys.setrecursionlimit(10000)
def count_letter(str, ch):
    if len(str) == 0:
        return 0
    else:
        if str[0] == ch:
            return 1+count_letter(str[1:], ch)
        else:
            return 0+count_letter(str[1:], ch)
string = input("Please enter a string\n")
character = input("Please enter a character\n") 
print(count_letter(string, character))
