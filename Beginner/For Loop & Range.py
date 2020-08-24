# A for loop is used for iterating over a sequence (that is either a
# list, a tuple, a dictionary, a set, or a string).
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print('\n')

#looping through a string
for x in "banana":
  print(x)
print('\n')

# break statement
for x in fruits:
  print(x) 
  if x == "banana":
    break
print('\n')

# continue statement
for x in fruits:
  if x == "banana":
    continue
  print(x)
print('\n')

# range() Function
for x in range(6):
  print(x)
print('\n')

#Using the start parameter:
for x in range(2, 6):
  print(x)
print('\n')

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)
print('\n')

# Else in For loop, else code is executed when the loop is finished
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print('\n')

# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of
# the "outer loop":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

