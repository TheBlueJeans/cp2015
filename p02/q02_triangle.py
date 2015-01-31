sides = []
sides.append(int(input("Please enter length of first side: \n")))
sides.append(int(input("Please enter length of second side: \n")))
sides.append(int(input("Please enter length of third side: \n")))
sides.sort()
if (sides[0]+sides[1])>sides[2] and side[0]!=0 and side[1]!=0 and side[2]!=0:
    print("The perimeter of the triangle is:", sides[0]+sides[1]+sides[2])
else:
    print("The triangle with the given sides does not exist")
