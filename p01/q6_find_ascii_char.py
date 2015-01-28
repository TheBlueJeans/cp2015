while True:
    number = input("Please enter an integer between 0 and 127:\n")
    if number.isdigit():
        integer = int(number)
        if -1 < integer <128:
            break
        else:
            print("Please input an integer where -1<integer<128")
    else:
        print("Please input an integer")
print("The character of an ASCII code is:", chr(integer))
