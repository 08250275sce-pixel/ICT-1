# count down timer
i = 10

while i >=1:
    print(i)
    i -= 1
print ("Times Up!")

#sum until zero

num = int(input("Enter the number to add and 0 to stop:"))
i = 0
while num != 0:
    i += num
    num = int(input("Enter the number to add and 0 to stop:"))
    
print("Total sum:", i)

# different way
i = 0 
while True:
    num = int(input("Entter the number to add and 0 to stop:"))

    if num == 0:
        break
    i += num
print ("Total Sum :",i)

# 3
i = 1
while i<= 3  :
    username = input("Enter User name:")
    password = input ("Enter you password:")

    if username == "admin" and password == "1234":
        print ("Login Sucessful!")
        break
    else:
        i -= 1
        print("wrong Youser name or password")

    if i == 0:
        print("Account Locked")


