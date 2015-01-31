names = []
scores = []
number = int(input("Please enter the number of students: \n"))
for i in range(0, number):
    names.append(input("Please enter the name of student {0}: \n".format(i+1)))
    scores.append(int(input("Please enter the score of student {0}: \n".format(i+1))))
topscore = max(scores)
topscorer = names[scores.index(topscore)]
scores.remove(topscore)
names.remove(topscorer)
print("The student with the highest scores is {0} with a score of {1}".format(topscorer, topscore))
print("The student with the second highest scores is {0} with a score of {1}".format(names[scores.index(max(scores))], max(scores)))
