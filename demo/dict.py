#dictionary
UserDetails = {'Id': 1, 'UserName:':'Sanja Dorji'}
print(type(UserDetails))
print(UserDetails)
location = dict(s = 'Samtse', t = 'Thimphu', p = 'Paro')
print(location)
print(UserDetails['UserName:'])
print(location.get('t'))
UserDetails['email'] = 'Jutme@gmail.com' # adding new key in userdetail
print(UserDetails)
UserDetails ['UserName:'] = 'just me updated'#updating existing value
print(UserDetails)
del location ['p']  #deleting a key-pair from the dictionary
print(location) # output : {'s': 'Samtse', 't': 'Thimphu'}}
deleted_values = UserDetails.pop('email') # this removes a key vlues pair and storing it in  deleted values
print(deleted_values)# just me@ gmail.com
del_key, del_values = UserDetails.popitem() # this removes the last item you insterted key-value pair and storing the removed key and value in separated variables
print(f'the deleted key is {del_key}and the deleted value is {del_values}')
location.clear() # removing all the key values of the fictionary location
print(location)