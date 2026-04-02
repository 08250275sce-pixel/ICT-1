name = str(input("Enter the student Name::"))
noofdaysB = int(input("Enter the number of days borrowed:"))
noofdaysL = int(input("enter the number days of the book late "))
# calculating fine
if noofdaysL == 0:
    fine = 0
    warning = "---"
elif noofdaysL >=5:
    fine = noofdaysL*5 
    warning = "pay the fine!"
elif noofdaysL >= 10 and noofdaysL <= 6:
    fine = noofdaysL* 10
    warning = "you over dued ! pay "
elif noofdaysL >= 10 and noofdaysL <= 29:
    fine = noofdaysL * 20 
    warning = "pay the fine and submmit on time"
else:
    fine = noofdaysL * 30 
    warning = "Libary previlages may be risticted!"
# output 
print("Library record of the student")
print("Student Name :", name)
print("Number of Days borrowed:", noofdaysB)
print("Number of days late:", noofdaysL)
print("Fine: Nu.",fine)
print ("warning:", warning)



