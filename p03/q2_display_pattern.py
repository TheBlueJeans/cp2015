def display_pattern(n):
    for i in range(0, n):
        pattern = ""
        for j in range(0, n):
            if i<n and j<i+1:
                pattern=pattern+"\t"+str(j+1)[::-1]
            else:
                pattern=pattern+"\t"
        print(pattern[::-1])
integer = int(input("Please input an integer\n"))
display_pattern(integer)
