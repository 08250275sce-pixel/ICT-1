def star(n): #defines the function star and n value tells how may rows will it take

    if n == 1: # base case
        print("* ") 
        print() # to create the spaces between two rows
    else:
        star(n-1) # recusive call it goes untilit reaches n == 1
        print("* " * n) # it prints n of stars 
        print()# to create the spaces between two rows
star(4)# calling this starts the function value from 4


    
    
    
