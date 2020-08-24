a = 60
b = 30
c = 70

# In this example a is greater than b, so the first condition is not true,
# also the elif condition is not true, so we go to the else condition
# and print to screen that "a is greater than b".
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# One line if else statement:
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")

# and operator
if a > b and c > a:
  print("Both conditions are True")
# or operator
if a > b or a > c:
  print("At least one of the conditions is True")
