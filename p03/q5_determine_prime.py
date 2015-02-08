def is_Prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range (3,int(n**0.5)+1,2):
        if (n%i==0):
            return False
    return True
integer = int(input("Enter a number\n"))
print(is_Prime(integer))
table = ""
prime = 1
number = 1
while prime<1001:
    if is_Prime(number) == True:
        table = table+str(number)+"\t"
        if prime%10 == 0:
            table = table+"\n"
        prime += 1
    number += 1
print(table)
