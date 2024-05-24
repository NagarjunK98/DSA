'''
Often, when dealing with iterators, we also need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task. The enumerate () method adds a counter to an iterable and returns it in the form of an enumerating object. This enumerated object can then be used directly for loops or converted into a list of tuples using the list() function.

We can use enumerate to get (index, value) pair while dealing with list or string
'''

'''
Here, we are using the enumerate() function with both a list and a string. Creating enumerate objects for each and displaying their return types. It also shows how to change the starting index for enumeration when applied to a string, resulting in index-element pairs for the list and string.
'''
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print ("Return type:", type(obj1))
print (list(enumerate(l1)))

# changing start index to 2 from 0
print (list(enumerate(s1, 2)))

# Output:
# Return type: <class 'enumerate'>
# [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]


'''
To get (index, value) pair
'''
s = "arjun"

for k, v in enumerate(s):
    print(k,v)

# Output
# 0 a
# 1 r
# 2 j
# 3 u
# 4 n
    

