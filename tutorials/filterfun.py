# syntax => filter(function, iterable)
# first argument of filter function is function ( must be single argument function)   and 2nd is iterable
# In Python 2.x, filter() returns list objects. This behavior changed in Python 3.x. Now the function returns a filter
# object, which is an iterator that yields items on demand. Python iterators are well known to be memory efficient.

def identity(x):
   return x


fun = identity(12)


objects = [0, 1, [], 4, 5, "", None, 8]
filter_obj=(filter(identity, objects))
print(filter_obj)