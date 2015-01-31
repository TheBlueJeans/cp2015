score = int(input("Please enter score between 0 and 100: \n"))
if 69<score<101:
    print("Your grade is: A")
elif 59<score<70:
    print("Your grade is: B")
elif 54<score<60:
    print("Your grade is: C")
elif 49<score<55:
    print("Your grade is: D")
elif 44<score<50:
    print("Your grade is: E")
elif 34<score<45:
    print("Your grade is: S")
elif -1<score<35:
    print("Your grade is: U")

else:
    print("Score has to be between 0 and 100")
