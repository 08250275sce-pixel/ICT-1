no_of_student = int(input("Enter the total number of students:"))
i = 1 # initalizing
students_name = {}# creating empty sets to store the names of the students
while i <= no_of_student: #conditions
    name = input("Enter the name of the student:") 
    i += 1 # incrementing the values of i by 1 in each iteration of the loop
    print("the name of the student {} is {}".format (i,name))
    students_name[i] =  name# it adds the name of the student to the dictionary student_ names withe the key values
print(students_name) # it prints dictionary

while True:
    print("This is continous loop press ctrl +c to stop")