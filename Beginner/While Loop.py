# The while loop we can execute a set of statements as long as a
# condition is true
i = 1
while i < 6:
  print(i)
  i += 1
print('\n')

# With the break statement we can stop the loop even if the while
# condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
print('\n')

# With the continue statement we can stop the current iteration,
# and continue with the next:
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
print('\n')

#This loop will print the last element and then delete it
names = ['Tom', 'Ellen', 'Sam']
while names:
    print(names.pop(), 'is going')
print('names =',names)
