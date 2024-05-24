'''
Python zip() method takes iterable containers and returns a single iterator object, having mapped values from all the containers. 

It is used to map the similar index of multiple containers so that they can be used just using a single entity. 
'''

'''
In Python, the zip() function is used to combine two or more lists (or any other iterables) into a single iterable, where elements from corresponding positions are paired together. The resulting iterable contains tuples, where the first element from each list is paired together, the second element from each list is paired together, and so on.
'''
name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]

# using zip() to map values
mapped = zip(name, roll_no)

print(set(mapped))
# Output - {('Nikhil', 1), ('Shambhavi', 3), ('Manjeet', 4), ('Astha', 2)}


'''
The combination of zip() and enumerate() is useful in scenarios where you want to process multiple lists or tuples in parallel, and also need to access their indices for any specific purpose.
'''
names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
	print(i, name, age)

# Output:
# 0 Mukesh 24
# 1 Roni 50
# 2 Chari 18


'''
result can be converted into list for dict
'''
k  = [1,2,3,4, 5]
v = ['a', 'b', 'c', 'd']

l = list(zip(k, v))
print("List result: ", l)

ll = dict(zip(k,v))
print("Dict result: ", ll)

# Output
# List result:  [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# Dict result:  {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

'''
Python’s zip() function can also be used to combine more than two iterables. It can take multiple iterables as input and return an iterable of tuples, where each tuple contains elements from the corresponding positions of the input iterables.
'''
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
result = list(zipped)
print(result)

# Output - [(1, 'a', 'x'), (2, 'b', 'y'), (3, 'c', 'z')]


'''
The zip() function will only iterate over the smallest list passed. If given lists of different lengths, the resulting combination will only be as long as the smallest list passed
'''
# Define lists for 'persons', 'genders', and a tuple for 'ages'
persons = ["Chandler", "Monica", "Ross", "Rachel", "Joey", "Phoebe", "Joanna"]
genders = ["Male", "Female", "Male", "Female", "Male", "Female", "Female"]
ages = (35, 36, 38, 34)

# Create a zipped object combining the 'persons' and 'genders' 
#lists along with the 'ages' tuple
zipped_result = zip(persons, genders, ages)

# Print the zipped object
print("Zipped result as a list:")
for i in list(zipped_result):
    print(i)

# Zipped result as a list:
# ('Chandler', 'Male', 35)
# ('Monica', 'Female', 36)
# ('Ross', 'Male', 38)
# ('Rachel', 'Female', 34)


'''
Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*” operator.
'''
# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)
# converting values to print as list
mapped = list(mapped)
# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

# unzipping values
namz, roll_noz, marksz = zip(*mapped)
print(namz)
print(roll_noz)
print(marksz)

# The zipped result is : [('Manjeet', 4, 40), ('Nikhil', 1, 50), 
# ('Shambhavi', 3, 60), ('Astha', 2, 70)]

# The name list is : ('Manjeet', 'Nikhil', 'Shambhavi', 'Astha')
# The roll_no list is : (4, 1, 3, 2)
# The marks list is : (40, 50, 60, 70)

'''
Using python loops
'''
players = ["Sachin", "Sehwag"]

# initializing their scores
scores = [100, 15]
# printing players and scores.
for pl, sc in zip(players, scores):
	print("Player : %s	 Score : %d" % (pl, sc))

# Output:
# Player :  Sachin     Score : 100
# Player :  Sehwag     Score : 15


