# defining the functions
def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return("Error!! number is not divisible by 0 it is undefined")
    return a / b


# displaying the menu operations
while True:
    print("Welcome to my Calculator")
    print("1. addition +")
    print("2. subtraction -")
    print("3. multiplication *")
    print("4. division /")
    print("5. Exit")

    Ab = input("Enter your choice (1-4) to do operations and 5 to exit: ")

# calcolator operations
    if Ab == "5":
        print("Thank you for using my calculator")
        break

    elif Ab == "1" or Ab == "2" or Ab == "3" or Ab == "4":

        n1 = float(input("Enter Number 1: "))
        n2 = float(input("Enter Number 2: "))

        if Ab == "1":
            print("Answer:", add(n1, n2))

        elif Ab == "2":
            print("Answer:", subtraction(n1, n2))

        elif Ab == "3":
            print("Answer:", multiplication(n1, n2))

        elif Ab == "4":
            print("Answer:", division(n1, n2))

    else:
        print("Wrong choice! Choose (1-4) for operations or 5 to exit")

