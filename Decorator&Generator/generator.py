# A generator in Python is a special type of iterator 
# that lazily yields values one at a time using yield, 
# instead of returning them all at once, saving memory.

def generator(n):

    value = 0

    while value<n:

        yield value

        value+=1

i = generator(4)

print(next(i))
print(next(i))
print(next(i))
print(next(i))

print('---------------------------------------------')
# create the generator object
cube_generator = (i * i * i for i in range(5))

# iterate over the generator and print the values
i = cube_generator

print(next(i))
print(next(i))
print(next(i))