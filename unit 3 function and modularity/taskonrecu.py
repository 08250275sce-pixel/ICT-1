# sunction x and y
def fun1(x,y):
    if x == 0:
        return y
    
    else:
        return fun1(x-1, x+y)
    
x = int(input("enter the value of x:"))
y =int(input("Enter the value of y:"))

print("answer:", fun1(x,y))