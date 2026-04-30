#for loops
name = input ("Enter the name:")
for i in name :
    print(i)
li = ["python programing","python fundamentals", "python interview questions"]
for x in li:# x is a variable that takes the value of each item in the list during each interation of the loop
    print(x)

lenli = len(li) # len() functions return the number of items li i.e.3.This valies is stored in the variable lenli
for x in range(lenli):
    print(li[x])

my_tuple = tuple(li)
print(my_tuple)
lentu = len(my_tuple)
for x in range(lentu):
    print(my_tuple[x])

my_set = set(li)
print(my_set)
for i in my_set:
    print(i)

tup = ("john Smith", "Jane Doe", "Alice Johnson")
for x in tup:
    print(x)

set1 = {10,30,20}
for x in set1:
    print(x)

BookDetails = dict({"Python Programing":"John Smith", "Python Fundamentals":"Alice Johnson", "Python Interviews Questions":"Jane Doe"})
for key in BookDetails:
    print(key,BookDetails[key])