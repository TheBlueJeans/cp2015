table="Miles\tKilometres\tKilometres\tMiles\n"
for i in range(1, 11):
    table=table+"{0}\t{1}\t\t{2}\t\t{3}\n".format(int(i), round(i*1.609, 3), 20+(i-1)*5, round((20+(i-1)*5)/1.609, 3))
print(table)
