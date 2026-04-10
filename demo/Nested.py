# nested loops
for i in range (1,4):#outer loops interact from 1 to 3
    for j in range(i):
        print (f"outer Loop iteration {i}, inner Loop iteration{j+1}")

for i in range (4): # it representas the number of row os stars to be printed. it iterates from 0 to 3, which means it willprint 4 rows of star
    for j in range(i):# it represents the number of stars to be printed in each row
        print("*", end = "")# endparameter is used to specify what toprint at the wnd of output by default, it is a new line character but here we are using space toprint the star
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

for i in range (6,0,-1):
    for j in range(i):
        print("*",end = " ")
    print()
      