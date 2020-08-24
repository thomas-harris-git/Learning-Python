thislist = ["apple", "banana", "cherry"]
print('thislist =',thislist)

thislist.reverse()
print("thislist.reverse():", thislist)
thislist.sort()
print("thislist.sort():", thislist)
print('len(thislist) =',len(thislist))

print('\n')
#Get Element
print("thislist[1] =", thislist[1])

#Change Element
thislist[1] = "blackcurrant"
print('thislist[1] = "blackcurrant": ',thislist)

#See if certain element exists in a List
thislist = ["apple", "banana", "cherry"]
print('thislist =',thislist)
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#Add Element
thislist.append("orange")
print('thislist.append("orange"):',thislist)
thislist.insert(2, "grape")
print('thislist.insert(2, "grape"):',thislist)

print('\n')
#Remove Element
thislist.remove("banana")
print('thislist.remove("banana"):',thislist)

# removes the specified index, (or the last item if index is not specified)
thislist.pop() 
print('thislist.pop():',thislist)

#Delete element at give index
del thislist[0]
print('del thislist[0]:',thislist)

# delete the list completely
del thislist

# clear list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print('thislist.clear():',thislist)

print('\n')
# Using the list() constructor to make a List
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print('thislist =',thislist)

# copy a list
list_copy = thislist.copy() 
print('list_copy =',list_copy)

# another way to copy a list
list_copy = list(thislist) 
print('mylist =',list_copy)

print('\n')
#Add the elements of cars to the fruits list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
print('fruits =',fruits)
print('cars =',cars)
fruits.extend(cars)
print('fruits.extend(cars):',fruits)

print('\n')
# Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
print('fruits =',fruits)
print('points =',points)
fruits.extend(points)
print('fruits.extend(points):',fruits)

