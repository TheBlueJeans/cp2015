table = "Miles\tKilometres\tKilometres\tMiles\n"
for i in range(1, 11):
    table = table+"{0}\t{1:<0.3f}\t\t{2}\t\t{3:<0.3f}\n".format(int(i), i*1.609, 20+(i-1)*5, (20+(i-1)*5)/1.609)
print(table)
