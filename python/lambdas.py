#sorting using lambda !!!
subject_marks=[('Maths',90),('English',88),('Science',95),('History',55)]
print(subject_marks)
subject_marks.sort(key=lambda x:x[1])
print(subject_marks)
##pascal
def pascal(n):
    row=[1]
    col=[0]
    for x in range (max(n,0)):
        print(row)
        row=[1+r for 1 , r in zip (row+col,col+row)]
    return n>=1
pascal(5)
#To get second lowest 
students = []
sec_name = []
second_low = 0 n = int(input("Input number of students: "))
for _ in range(n):
s_name = input("Name: ")
score = float(input("Grade: "))
students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
if order[i][1] != order[0][1]:
second_low = order[i][1]
break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
print(s_name)

#extract n elements
def extract_nth_element(test_list, n):
result = list(map (lambda x:(x[n]), test_list))
return result
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
print ("Original list:")
print(students)
n = 0
print("\nExtract nth element ( n =",n,") from the said list of tuples:")
print(extract_nth_element(students, n))
n = 2
print("\nExtract nth element ( n =",n,") from the said list of tuples:")
print(extract_nth_element(students, n))
#Baiscs!

r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))

##sqaure the list

def printValues():
l = list()
for i in range(1,21):
l.append(i**2)
print(l)
printValues()

#perfect square or not
def perfect_number(n):
sum = 0
for x in range(1, n):
if n % x == 0:
sum += x
return sum == n
print(perfect_number(6))
