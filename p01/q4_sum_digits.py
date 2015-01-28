while True:
    number = input("Please enter an integer that is between 0 and 1000: \n")
    if number.isdigit():
        integer = int(number)
        if -1 < integer < 1001:
            break
        else:
            print("Please input an integer where -1<integer<1001")
    else:
        print("Please input an integer")
sum = 0
for digit in number:
    sum += int(digit)
print("The sum of all the digits is:", sum)
