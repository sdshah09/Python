value = []
value.append(25) #! add value to the list
print(value)

value.extend([35,34,32,31,'Shaswat']) #todo add multiple values to the list
print(value)

print(value.pop(2)) #! just like stack it will pop out the last value.
print(value)


value.remove(31) #? will remove any value you mentioned
print(value)

del value[2] #! willl delete the particular index value or upto the index you want
print(value)

value.insert(2,'hii') #? insert any value at particular index
print(value)

value[1] = 55 #! mutable so directly assign value to the index
print(value)

value.clear() #todo clear the whole list
print(value)