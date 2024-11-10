'''
Iterator:
    1. Iterators are objects that can be iterated upon
    2. Any object that can derive an iterator is known as an iterable
    3. For instance, the implementation of each iterator object must consist of an __iter__() and __next__() method.
    4.  In addition to the prerequisite above, the implementation must also have a way to track the object's internal state and raise a StopIteration exception once no more values can be returned. These rules are known as the iterator protocol
    5. Implementing your own iterator is a drawn-out process, and it is only sometimes necessary. A simpler alternative is to use a generator object. Generators are a special type of function that use the yield keyword to return an iterator that may be iterated over, one value at a time. 
    6. Iterables are objects capable of returning their members one at a time – they can be iterated over
    7. The values obtained from an iterator can only be retrieved from left to right. Python does not have a previous() function to enable developers to move backward through an iterator.
'''

# Example

list = [1,2,3]
list_itr = iter(list)
print(next(list_itr)) # return 1
print(next(list_itr)) # return 2
print(next(list_itr)) # return 3
print(next(list_itr)) # return error saying StopIteration

list = [1,2,3]
list_itr = iter(list)
for ele in list_itr:
    print(ele) # When the StopIteration exception is caught, then the loop ends

'''
Generator:
    1. The most expedient alternative to implementing an iterator is to use a generator
    2. Although generators may look like ordinary Python functions, they are different. For starters, a generator object does not return items. Instead, it uses the yield keyword to generate items on the fly
    3. Thus, we can say a generator is a special kind of function that leverages lazy evaluation
    4. Generators do not store their contents in memory as you would expect a typical iterable to do
    5. Since we use the yield keyword instead of return, the function will not exit after the run. In essence, we told Python to create a generator object instead of a traditional function, which enables the state of the generator object to be tracked
'''

# Example

def generator(N):
    for ele in range(1, N):
        yield ele%7

N = 3

res = generator(N)
print(next(res)) # return 1
print(next(res)) # return 2
print(next(res)) # return StopIteration exception

# Another way
def generator(N):
    for ele in range(1, N):
        yield ele%7

N = 3
res = generator(N)

for ele in res:
    print(next(ele)) # When the StopIteration exception is caught, then the loop ends


# iterator vs generator
'''
Iterator:
    - Class is used to implement an iterator
    - Local Variables aren't used here.
    - Iterators are used mostly to iterate or convert other objects to an iterator using iter() function
    - Iterator uses iter() and next() functions 
    - Every iterator is not a generator

Generator:
    - Function is used to implement a generator.
    - All the local variables before the yield function are stored. 
    - Generators are mostly used in loops to generate an iterator by returning all the values in the loop without affecting the iteration of the loop
    - Generator uses yield keyword
    - Every generator is an iterator
'''

# https://www.geeksforgeeks.org/difference-between-iterator-vs-generator/
# https://www.datacamp.com/tutorial/python-iterators-generators-tutorial