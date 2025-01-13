from collections import namedtuple
number_of_students = int(input())
navbars = list(map(str, input()))
students = namedtuple('students', "".join(navbars))
marks = []
for i in range(number_of_students):
    val1, val2, val3, val4 = map(str, input().split())
    list_of_students = students(val1, val2, val3, val4)
    marks.append(int(list_of_students.MARKS))

print(f'{sum(marks)/len(marks):.2f}')