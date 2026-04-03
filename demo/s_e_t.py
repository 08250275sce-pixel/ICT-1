# set example
my_set = {1,2,3,'Hello',3.15,1,2,False}# dupcalitae values will be removed
print(type(my_set)) # Data Type of my_set is set
print(my_set)# the order msy vsry
#my_set[0] = "start" # this will raise an error because sets are unordered and donot suppor indexing
my_set.add("World")
print(my_set)#{False, 1, 2, 3.15, 3, 'Hello', 'World'} output and the order may vary
my_second_set = {3,4,5}
union_set = my_set.union(my_second_set)
print(union_set)
intersection_set = my_set.intersection(my_second_set)
print(intersection_set)
difference_set = my_set.difference(my_second_set)
print(difference_set)
my_set.clear()
print(my_set)
