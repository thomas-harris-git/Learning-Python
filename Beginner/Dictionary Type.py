# A dictionary is a collection which is unordered, changeable and indexed.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print('thisdict =',thisdict)

# You can access the items of a dictionary by referring to its key name,
# inside square brackets:
x = thisdict["model"]
print('thisdict["model"]:',x)

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print('thisdict.get("model"):',x)

# You can change the value of a specific item by referring to its key name:
thisdict["year"] = 2018
print('thisdict["year"] = 2018:',thisdict)

print('\n')
#You can loop through a dictionary by using a for loop.
#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

print('\n')
# Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])

print('\n')
# You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
  print(x)

print('\n')
#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)

print('\n')
# To determine if a specified key is present in a dictionary use the in keyword:
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# To determine how many items (key-value pairs) a dictionary has, use the
# len() method.
print('len(thisdict) =',len(thisdict))

# Adding an item to the dictionary is done by using a new index key and
# assigning a value to it or using the update() method:
thisdict["color"] = "red"
print('thisdict["color"] = "red":',thisdict)
thisdict.update({"fuel": "Petrol"})
print('thisdict.update({"fuel": "Petrol"}):',thisdict)

print('\n')
# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print('thisdict.pop("model"):',thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7,
# a random item is removed instead):
thisdict.popitem()
print('thisdict.popitem():',thisdict)

# The del keyword removes the item with the specified key name:
del thisdict["year"]
print('del thisdict["year"]:',thisdict)

# The clear() keyword empties the dictionary:
thisdict.clear()
print('thisdict.clear():',thisdict)

# The del keyword can also delete the dictionary completely:
del thisdict #printing will cause an error because it no longer exists

print('\n')
# It is also possible to use the dict() constructor to make a new dictionary:
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print('thisdict =',thisdict)

# You cannot copy a dictionary simply by typing dict2 = dict1, because:
# dict2 will only be a reference to dict1, and changes made in dict1 will
# automatically also be made in dict2.
# Make a copy of a dictionary with the copy() or dict() method:
mydict = thisdict.copy()
print('mydict = thisdict.copy():',mydict)
mydict = dict(thisdict)
print('mydict = dict(thisdict):',mydict)

print('\n')
# The keys() method returns a view object. The view object contains the keys
# of thedictionary, as a list.
print('thisdict.keys() =',thisdict.keys())

# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value, see
# example below
print('thisdict.setdefault("model", "Bronco") =',thisdict.setdefault("model", "Bronco"))
print('thisdict.setdefault("color", "White") =',thisdict.setdefault("color", "White"))
print('thisdict =',thisdict)

print('\n')
#The fromkeys() method returns a dictionary with the specified keys and values.
x = ('key1', 'key2', 'key3')
y = 1
print('x =',x)
print('y =',y)
thisdict = dict.fromkeys(x, y) #if no value is given the defult is 'None'
print('dict.fromkeys(x, y):',thisdict)

