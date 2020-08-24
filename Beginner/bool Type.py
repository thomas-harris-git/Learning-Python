# The only two instances of the boolean class ar True or False
x, y = 1, 0
print('bool(x) =', bool(x))
print('bool(y) =', bool(y))
# The bool class is a subclass of 'int'

# Zero values are considered false, non-zero True
# Values that are considered false in Python:
None
False
0 or 0.0 or 0j
'' or [] or () #empty sequences are false
{} or set([])  #empty mappings are false

#Boolean Or returns first True, or last False value
print('True or False returns', True or False)
print('1 or 0 returns', 1 or 0)
print('None or 0 returns', None or 0)

#Boolean And returns first False, or last True value
print('True and False returns', True and False)
print('1 and 0 returns', 1 and 0)
print('None and 0 returns', None and 0)

#Boolean Not returns False, if operand is True
print('not True returns', not True)
print('not 1 returns', not 1)
print('not "text" returns', not "text")

#Boolean Not returns True, if operand is True
print('not False returns', not False)
print('not 0 returns', not 0)
print('not "" returns', not "")
