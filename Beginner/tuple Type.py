# A tuple is a collection which is ordered and unchangeable
thistuple = ("apple", "banana", "cherry")
print('thistuple =',thistuple)
# You can access tuple items by referring to the index number
print('thistuple[1] =',thistuple[1]) 
print('len(thistuple) =',len(thistuple))
del thistuple # delete tuple
thistuple = tuple(("apple", "banana", "cherry"))#note the double round-brackets
print('thistuple =',thistuple)
print('thistuple.count("apple") =', thistuple.count('apple'))
print('thistuple.index("apple") =', thistuple.index('apple'))
