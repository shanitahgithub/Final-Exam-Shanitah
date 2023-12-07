# No.3 i)
age=int(input('Enter your age:'))
if age >=18:
    print('You are eligible')
else:
    print('You are not eligible')
    
# ii) grade students
mark=int(input('Enter student mark:'))
def grade_students(mark):
    
    if mark >=90:
        print('Grade A')
    elif mark >=80 and mark <=89:
        print('Grade B')
    elif mark >=70 and mark <=79:
        print('Grade C')
    elif mark >=60 and mark <=69:
        print('Grade D')
    else:
        print('Grade F')
grade_students(mark)

#iv)
mark=input('Enter student mark:')
def grade_students(mark):
    for x in mark:
        if x!=mark:
            print('Invalid Input')
        else:
            print('Valid Input')
grade_students(mark)

# v) message along with the grade

mark=int(input('Enter student mark:'))
def grade_students(mark):
    
    if mark >=90:
        print('Grade A')
        print('Excellent')
    elif mark >=80 and mark <=89:
        print('Grade B')
        print('Excellent')
    elif mark >=70 and mark <=79:
        print('Grade C')
        print('Good')
    elif mark >=60 and mark <=69:
        print('Grade D')
        print('Satisfactory')
    else:
        print('Grade F')
        print('Needs Improvement')
grade_students(mark)
            
