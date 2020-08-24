# Slicing allows access to one of more elements of a sequence
a_tuble = ('a',1,2,(3,4))
a_string = 'immutable'
a_list = [5,6,7,8,(4,5)]
print('a_tuble =',a_tuble)
print('a_string =',a_string)
print('a_list =',a_list)

# Accessing an element
print('a_tuble[0] =',a_tuble[0])
print('a_string[1] =',a_string[1])
print('a_list[2] =',a_list[2])

# Can Use Negaive Indexes
print('a_tuble[-1] =',a_tuble[-1])
print('a_string[-2] =',a_string[-2])
print('a_list[-3] =',a_list[-3])

# Subslice of a sequence
print('a_list[0:2] =',a_list[0:2])
print('a_list[:2] =',a_list[:2])
print('a_list[2:5] =',a_list[2:5])
print('a_list[2:] =',a_list[2:])
print('a_list[:] =',a_list[:])

# Add a third parameter for steps
print('a_list[::2] =',a_list[::2])
print('a_list[1:4:2] =',a_list[1:4:2])
print('a_list[::-1] =',a_list[::-1])

# Use additional slices to access elements with sequwnces
print('a_list[4] =',a_list[4])
print('a_list[4][0] =',a_list[4][0])
print('a_list[4][0] =',a_list[4][1])

# Sequences can be updated with slices
print('a_list =',a_list)
a_list[0] = 'five'
print('a_list =',a_list)
a_list[1:4] = [10,11,12]
print('a_list =',a_list)

# A slice object can also be used
a_slice = slice(4)
print('a_slice =',a_slice)
print('a_list[a_slice] =',a_list[a_slice])
a_slice = slice(1,5)
print('a_slice =',a_slice)
print('a_list[a_slice] =',a_list[a_slice])
a_slice = slice(1,5,2)
print('a_slice =',a_slice)
print('a_list[a_slice] =',a_list[a_slice])


