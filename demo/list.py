my_list =[1,2,3,"Hello",3.14,True]
my_repated_list =[3]*3
print (my_list) # output [1,2,3,"Hello",3.14,True]
print(type(my_list)) # datta type will be list
print(my_repated_list)
print(my_list[-1])# locating index index start with 0 1 2 and so on
my_list.append("world")# append add only one word orr list in the end of the list outout [1, 2, 3, 'Hello', 3.14, True, 'world']
print (my_list)
my_list.extend([4,5,6])# add multiple list
print(my_list)
my_list.insert(0, "Start") # insert new list at specific index
print(my_list)
my_list.remove(3) # in bracket its not the index it just remove the like 3 or hello
print(my_list)
my_list.pop()#IT REMOVES ONLY THR LAST ELEMENT IN THE LAST
print(my_list)
del my_list[-1]# delete it fronm specific using index
print(my_list)
my_repated_list.clear()
print(my_repated_list)
my_list[6] = "Hy"
del my_list[5]
my_list.insert(5,False)
print (my_list)