

#Return an iterator that applies function to every item of iterable, yielding the results.
#first agrument of map is function and second agrument is iteable

def square(num):
    return num**2

numlist= [1,2,3,4]
squared = map(square, numlist)

output= list(squared)

print(output)