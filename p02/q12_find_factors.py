number = int(input("Please enter number: \n"))
factors = ""
for i in range (2, int(number/2)+1):
    while number%i==0:
        factors = factors+"{0}, ".format(i)
        number=number/i
print(factors)

