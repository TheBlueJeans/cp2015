table="Kilograms Pounds\n"
for i in range(1, 11):
    table=table+"{0}  \t  {1}\n".format(int(i), int(i*2.2))
print(table)
