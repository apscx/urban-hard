
grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}

list_students = sorted(list(students))
dict_avg_grades = {}

n_student = 0
for grade in grades:
    list_grade = list(map(int,grade.split()))
    dict_avg_grades[list_students[n_student]] = sum(list_grade)/len(list_grade)
    n_student += 1

print(dict_avg_grades)