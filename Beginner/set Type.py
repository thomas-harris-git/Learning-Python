# A set is a collection which is unordered and unindexed.
thisset = {"apple", "banana", "cherry"}
print('thisset =',thisset)

print('\n')
#Loop through the set, and print the values:
for x in thisset:
  print(x)

print('\n')
# Check if "banana" is present in the set:
print("banana" in thisset)

print('\n')
# Add an item to a set, using the add() method:
thisset.add("orange")
print('thisset.add("orange"):',thisset)

# Add multiple items to a set, using the update() method:
thisset.update(["mango", "grapes"])
print('thisset.update(["mango", "grapes"]):',thisset)

print('\n')
# Get the length of a set
print('len(thisset) =',len(thisset))

print('\n')
# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print('thisset =',thisset)

# Remove "banana" by using the remove() method:
# If the item to remove does not exist, remove() will raise an error.
thisset.remove("banana")
print('thisset.remove("banana"):',thisset)

# Remove "apple" by using the discard() method:
# If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("apple")
print('thisset.discard("apple"):',thisset)

print('\n')
# You can also use the pop(), method to remove an item, but this method
# will remove the last item. Remember that sets are unordered, so you will
# not know what item that gets removed.
thisset = {"apple", "banana", "cherry"}
print('thisset =',thisset)
x = thisset.pop()
print('thisset.pop() =',x)
print('thisset =',thisset)

# The clear() method empties the set:
thisset.clear()
print('thisset.clear():',thisset)

# The del keyword will delete the set completely:
del thisset
print('\n')

#Return a set that contains the items that only exist in set x, and not in set y:
x = {1, 4, 3, 2, 9}
y = {5, 6, 3, 1, 8}
print('x =',x)
print('y =',y)
z = x.difference(y) 
print('x.difference(y) =',z)

#Remove the items that exist in both sets:
x.difference_update(y) 
print('x.difference_update(y) =',x)

# The intersection() method returns a set that contains the similarity between
# two or more sets.
print('\n')
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
print('x =',x)
print('y =',y)
print('y =',z)
result = x.intersection(y, z)
print('x.intersection(y, z) =',result)

print('\n')
# The intersection_update() method removes the items that is not present in both
# sets (or in all sets if the comparison is done between more than two sets).
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print('x =',x)
print('y =',y)
x.intersection_update(y) 
print('x.intersection_update(y) =',x)

print('\n')
# The isdisjoint() method returns True if none of the items are present in both
# sets, otherwise it returns False.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
print('x =',x)
print('y =',y)
z = x.isdisjoint(y) 
print('x.isdisjoint(y) =',z)

print('\n')
# The issubset() method returns True if all items in the set exists in the
# specified set, otherwise it retuns False.
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
print('x =',x)
print('y =',y)
z = x.issubset(y) 
print('x.issubset(y) =',z)

# The issuperset() method returns True if all items in the specified set
# exists in the original set, otherwise it retuns False.
z = y.issuperset(x) 
print('y.issuperset(x) =',z)

print('\n')
# The symmetric_difference() method returns a set that contains all items from
# both set, but not the items that are present in both sets.
# Meaning: The returned set contains a mix of items that are not present in
# both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print('x =',x)
print('y =',y)
z = x.symmetric_difference(y) 
print('x.symmetric_difference(y) =',z)

# The symmetric_difference_update() method updates the original set by
# removing items that are present in both sets, and inserting the other items.
x.symmetric_difference_update(y)
print('x.symmetric_difference_update(y) =',x)

print('\n')
# The union() method returns a set that contains all items from the original
# set, and all items from the specified sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print('x =',x)
print('y =',y)
z = x.union(y) 
print('x.union(y) =',z)

