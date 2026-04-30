# fuctions calls itself directlyor indirectly is called recursion
# define base case and recursion case
# sum of natural numbers using recursive function
def sum(n):

    if n == 1: #base case
        return 1
    else: #recursive call
        return n + sum(n-1)
    
n = int(input("Enter a number:"))
print ("sum of numbers from 1 to ",n,"is:", sum(n))

# find the factrioal of (5)
def fact(n):

    if n == 0: # base case
        return 1
    
    else: # recursive call
        return n * fact(n-1)
    
print ("Factorial of 5 is :", fact(5))


