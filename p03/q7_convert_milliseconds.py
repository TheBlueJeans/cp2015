def convert_ms(n):
    time=""
    multiples = [3600000, 60000, 1000]
    for i in range(0, 3):
        if n/multiples[i] > 0:
            print(n/multiples[i])
            time = time+str(n//multiples[i])+":"
            n = n%multiples[i]
        else:
            time = time+"0:"
    return time[:-1]
integer = int(input("Enter a number\n"))
print(convert_ms(integer))
