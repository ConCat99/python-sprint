import csv
from collections import namedtuple

from numpy.ma.extras import average

records =[]
average_grades = 0

with open('student_grades.csv', 'r', newline='') as cf:
    reader = csv.DictReader(cf)
    for row in reader:
        records.append(row)

# print(records)

grades= [int(grade['Grade']) for grade in records]
# print(grades)

average_grades=sum(grades)/len(grades)
print(average_grades)


