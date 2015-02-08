import random
def print_matrix(n):
    matrix = [[None for x in range(n)] for x in range(n)] 
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = random.randint(0, 1)
    for row in matrix:
        print(" ".join(map(str,row)))
integer = int(input("Please enter an integer\n"))
print_matrix(integer)
