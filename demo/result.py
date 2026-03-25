#get the input from users
English=float(input("Enter the marks of English:"))
Dzongkha=float(input("Enter the marks of Dzongkha:"))
Maths=float(input("Enter the marks of Maths:"))
Science=float(input("Enter the marks of Science:"))
#calculate the totalmarks
T = English + Dzongkha + Maths + Science
#calculate the percentage
P = (T/400)*100
print("Total Marks:",T)
print("Percentage:",P,"%")
#check the grade using logicsal operator "or"
if P >= 90 or P >= 80 or P >= 70 or P >= 60:
    print("Grade:A+")
elif P >= 50 or P >= 40:
    print("Grade:B+")
else :
    print("Grade:C")
#checking pass or fail using "and"
if P >= 40 and English >= 40 and Dzongkha >= 40 and Maths >= 40:
    print("Status:Passམཐར་འཁྱོལ་ནུག","/nRemarks:good")
else:
    print("Status:Fail མཐར་འཁྱོལ་མ་ཚུགས།","/nRemarks:work hard")
#commenting on result using logical operter

    
    



