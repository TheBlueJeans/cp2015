number1 = int(input("Please enter the first number: \n"))
number2 = int(input("Please enter the second number: \n"))
gcd=min(number1, number2)
while number1%gcd!=0 or number2%gcd!=0:
    gcd-=1
print("The greatest common divisor for {0} and {1} is {2}".format(number1, number2, gcd))
