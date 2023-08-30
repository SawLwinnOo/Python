from functools import reduce

# syntax => reduce( function, iterable )
#

my_reduce= reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
print(my_reduce)
