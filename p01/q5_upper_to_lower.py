while True:
    uppercase = input("Please enter an uppercase letter: \n")
    if len(uppercase) == 1:
        if uppercase.isupper():
            break
        else:
            print("Please input a upper letter")
    else:
        print("Please input only one upper letter")
print("Lowercase letter of the letter above is:", chr(ord(uppercase)+32))
