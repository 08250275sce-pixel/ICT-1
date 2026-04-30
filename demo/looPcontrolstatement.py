#break statement
for i in range (4):
    if i == 2:
        break# the break statement is used to exit the loop when the value of i is eaual to 2
    print(i)
print("loop ended")

# continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)
print("Loop ended")