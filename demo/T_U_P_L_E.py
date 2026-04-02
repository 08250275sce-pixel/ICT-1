my_tuple = ('Hello', 123456)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[1])
a, b =(my_tuple) # unpacking the my_tuple
print(a)
new_t = tuple(a) # converting string 'Hello to a tuple of characters'
print(new_t)
concatenated_tuple = my_tuple + new_t
print(concatenated_tuple)# output will be ('Hello', 123456, 'H', 'e', 'l', 'l', 'o')
print(concatenated_tuple[2:6:2])# [start:stops:Step] output ('H','l')
print(concatenated_tuple[::-1]) # ('o', 'l', 'l', 'e', 'H', 123456, 'Hello') output
del my_tuple # delete my tuple
print(my_tuple)# error because m_tuple was deleted 

