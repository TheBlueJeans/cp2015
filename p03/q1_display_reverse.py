def reverse_int(n):
    reverse = [""]*len(n)
    for i in range(0, len(n)):
        reverse[-i-1] = n[i]
    print("".join(reverse))
integer = input("Please enter an integer\n")
reverse_int(integer)
