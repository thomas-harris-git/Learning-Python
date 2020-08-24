x = 5
y = 10
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

# Bitwise operators
print('Or: x | y =', x | y)
print('Xor: x ^ y =', x ^ y)
print('And: x & y =', x & y)
print('Left shift: x << y =', x << y)
print('Right shift: x >> y =', x >> y)
print('Inversion: ~x =', ~x)


