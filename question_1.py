
# i) Area of the circle
def calculate_area():
    raduis_of_a_circle=int(input("Enter the radius of a circle: "))
    area_of_the_circle=3.14*(raduis_of_a_circle)**2
    print(area_of_the_circle)
calculate_area()

def calculate_area(raduis_of_a_circle):
    area_of_the_circle=3.14*(raduis_of_a_circle)**2
    print(area_of_the_circle)
calculate_area(5)


# iii)
numbers=[1,3,5,7,9]
numbers.pop(2)
print(numbers)    # removing element at index 2

numbers.append(10)
print(numbers)    # inserting the value 10 at the end

# iv)
even_numbers=[2,4,6,8,10]
new_list=[]
new_list.append(even_numbers)
print(new_list)               #creating new list

# v)
student_info={'name':'Alice','age':20,'grade':'A'}
student_info['age']=25
print(student_info)    # updating the value of age to 25



# ii)
natural_numbers=[1,2,3,4]
def sum(natural_numbers):
    total=0
    for x in natural_numbers:
        total+=x
    return total
sum(natural_numbers)
print(f'The sum of natural numbers is {sum(natural_numbers)}')
    
