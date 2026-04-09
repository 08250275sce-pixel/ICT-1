# first get the input from users
Name = str(input("Enter Your Name:"))
M1 = float(input("Enter Your Module1 marks"))
M2 = float(input("Enter Your Module2 marks"))
M3 = float(input("Enter Your Module3 marks"))
M4 = float(input("Enter Your Module4 marks"))
Attendance = float(input("enter your attendance:"))
# print output for name and attandance
print("Name:",Name)
print(f"Attendence:{Attendance}%")
#processs find percentage
T= (M1+M2+M3+M4)
P= (T/400)*100
#printing percantage
print("Percentage:%.2f" %(P),"%")
#checking Status
if P>=40 and Attendance>=80 and M1>=40 and M2 >= 40 and M3 >=40 and M3>=40:
    print("Status:Passམཐར་འཁྱོལ་ནུག")
    
else:
    print("Status:Fail མཐར་འཁྱོལ་མ་ཚུགས།")
#using conditions finding Grade
if P>=90 and Attendance>=80 and M1>=90 and M2 >=90 and M3>=90 and M4>=90:
    print("Grade:A [Excellent]. \n You are elible forreward.")
elif P>=75 and Attendance>=80 and M1>=75  and M2>=75 and M3>=75 and M4>=75:
    print("Grade:B[Very Good]")
elif  P>=60 and Attendance>=80 and M1>=60  and M2>=60 and M3>=60 and M4>=60:
    print("Grade:C[Good]")
elif  P>40 and Attendance>=80 and M1>=40  and M2>=40 and M3>=40 and M4>=40:
    print("Grade:D[Standard]")
else:
    print("Grade F[NEED IMPROVEMENT!!!]")
#Cheking eligibility for Reward
if Attendance >= 80 and P>=80 or P>=90:
    print("Eligibilty for Reward:YES")
else:
    print("Eligibilty for Reward:NO" )
    