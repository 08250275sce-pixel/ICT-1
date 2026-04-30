# initialize empty lists and dictionary
students_list = [] # it stores only the name of students just for easy indexing
student_dict = {} # it will stores age,grade and id 
#adding few student and their details
students_list.append("Olo Penjor")
student_dict["Olo penjor"] = {"Age": 18, "Grade": "A", "Student_id": 201001}

students_list.append("Soto")
student_dict["Tashi"] = {"Age": 19, "Grade": "B", "Student_id": 201002}

students_list.append("Tawla ")
student_dict["Tawla"] = {"Age": 17, "Grade": "A+", "Student_id": 201003}

students_list.append("Gongdho Dorji")
student_dict["Gongdho Dorji"] = {"Age": 18, "Grade": "B+", "Student_id": 201004}

# asking the prompt from the users
name =  input("Enter the student Name:")
age  = int(input("Enter the student age:"))
grade = input("Enter the student Grade:")
std_id = int(input("Enter the student id:"))
# now we have to add name in the list and age grade and std_id to std dictionary using append and add
students_list.append(name) # this function will add the name in the list
student_dict[name] = {'Age': age, "Grade": grade, "Student_id":std_id}# add the age grade and std id to std dict using key name fromlist

# now printing sucess message studen display 
print (f"sucess !!{name} your name added to system sucessfully! ")
print("Current student dictionary:", student_dict)

# Now search for student from management list
search_student = input("Enter the name of the Student:")# Take input from the user (student name to search)
if search_student in students_list:# this code checks if the entered name from the user is there in the student list
    print(f"Student found!!{search_student}")#if found then print success message
    print(f"Student Details: {student_dict[search_student]}")# Print student details from dictionary using the name as key
else:
    print("Student Not Found")# if not print not found

# Removing student
remove_student = input("Enter the name of student you want to remove: ")# asking from the users

if remove_student in students_list:
    students_list.remove(remove_student)   # remove name from list
    del student_dict[remove_student]       # remove details from dictionary using key
    print(" student removed successfully!")
else: 
    print("Student not found")


    




