x = 5.0
y = 10.0
print('x =', x, ',', 'y =', y)

# Typical comparisons:
print('x == y =', x == y)
print('x != y =', x != y)
print('x >= y =', x >= y)
print('x > y =', x > y)
print('x <= y =', x <= y)
print('x < y =', x < y)

# The usual operators:
print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x / y =', x / y)

# In Python 2, x / y uses floor division like:
print('x // y =', x // y)
print('x % y =', x % y)
print('x ** y =', x ** y)

# buitin functions:
print('divmod(x, y) =', divmod(x, y))
print('pow(x, y) =', pow(x,y))
print('abs(-x) =', abs(-x))
print('int(5.2) =', int(5.2))
print('int("0xff",16) =', int("0xff",16))
print('float(x) =', float(x))

# Inline notation can also be used:
print('x = x + y =', end = ' ')
x += y
print(x)
print('x = x - y =', end = ' ')
x -= y
print(x)
print('x = x * y =', end = ' ')
x *= y
print(x)
print('x = x / y =', end = ' ')
x /= y
print(x)

# Multiple Assignments:
x, y = 4, 2
print('x =', x, ',', 'y =', y)
