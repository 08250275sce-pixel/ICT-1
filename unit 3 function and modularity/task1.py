m1 = float(input("Enter marks 1:"))
m2 = float(input("Enter marks 2:"))
m3 = float(input("Enter marks 3:"))

def total(m1,m2,m3):
    return(m1+m2+m3)

print("total:",total(m1,m2,m3))

def avg(m1,m2,m3):
    return((m1+m2+m3)/3)
print("Average:",avg(m1,m2,m3))

def result(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"
print("Result:",result(avg(m1,m2, m3)))

#Even and ODD number

num = int(input("Enter any Number you Like:"))
def number(num):
    if num % 2 == 0 and num < 0:
        return("Number is Even and negative integer")
    elif num % 2 == 0 and num > 0:
        return("Number is Even and positive integer")
    elif num % 2 != 0 and num < 0:
        return "Number is Odd and Negative integer"
    else:
        return("Number is Odd and positive integer")
print(number(num))