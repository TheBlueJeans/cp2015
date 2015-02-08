def m(i):
    sum = 0
    series = []
    for j in range(1, i+1):
        sum = sum+j/(j+1)
        series.append(sum)
    return series
def m_series(n):
    print(m(n)[-1])
integer = int(input("Please enter an integer\n"))
m_series(integer)
table = "i\tm(i)\n"
for x in range(0, integer):
    table = table+"{0}\t{1:<0.4f}\n".format(integer, round(m(integer)[x], 4))
print(table)
