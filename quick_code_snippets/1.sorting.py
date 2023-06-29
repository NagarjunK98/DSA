'''
sorted method: 

Its syntax is: sorted(iterable, key=key, reverse=reverse)

    1. The sorted() method sorts iterable data such as lists, tuples, and dictionaries, string, sets. But it sorts by key only
    2. The sorted() method puts the sorted items in a list.
    3. If you use the sorted() method with a dictionary, only the keys will be returned and as usual, it will be in a list
    
Parameters of the sorted() Method
The sorted() method can accept up to 3 parameters:
    1. iterable – the data to iterate over. It could be a tuple, list, or dictionary.
    2. key – an optional value, the function that helps you to perform a custom sort operation.
    3. reverse – another optional value. It helps you arrange the sorted data in ascending or descending order

Key points
    1. The sorted() function in Python uses an algorithm called Timsort, which is a hybrid sorting algorithm 
    derived from merge sort and insertion sort
    2. Timsort performs well on many kinds of real-world data and is designed to take advantage of existing order or partial order
    in the input
    3. The average-case time complexity of Timsort is O(n log n), where n is the number of elements in the input list.
    4. In the worst case, Timsort has a time complexity of O(n log n). This occurs when the input list is in reverse order, 
    as Timsort needs to perform more comparisons and swaps to sort the list.
    5. The best-case time complexity of Timsort is O(n), which occurs when the input list is already sorted or nearly sorted. 
    In such cases, Timsort can take advantage of the existing order and perform fewer comparisons and swaps
    
Applications:
    1. Use to sort list, tuple, dict(by value or by key)
'''
# sorted - list
persons = ['Chris', 'Amber', 'David', 'El-dorado', 'Brad', 'Folake']
sortedPersons = sorted(persons)
print(sortedPersons)
# Output: ['Amber', 'Brad', 'Chris', 'David', 'El-dorado', 'Folake']

# sorted - tuple
numbers = (14, 3, 1, 4, 2, 9, 8, 10, 13, 12)
sortedNumbers = sorted(numbers)
print(sortedNumbers)
# Output: [1, 2, 3, 4, 8, 9, 10, 12, 13, 14]

# sorted - dict
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sortedDict = sorted(my_dict)
print(sortedDict)
# ['num1', 'num2', 'num3', 'num4', 'num5', 'num6']

# To get dictionary as result after sorting by value or key (0-> by key, 1-> by value)
my_dict = { 'num6': 6, 'num3': 3, 'num2': 2, 'num4': 4, 'num1': 1, 'num5': 5}
sorted_list = sorted(my_dict.items(), key = lambda x:x[1], reverse=True) # returns sorted list of tuples(k,v) 
sorted_dict = dict(sorted_list)

# sorted - string
x = "python"
print(sorted(x))
# ['h', 'n', 'o', 'p', 't', 'y']

# sorted - set
x = {'q', 'w', 'e', 'r', 't', 'y'}
print(sorted(x))
# ['e', 'q', 'r', 't', 'w', 'y']

# sorted - based on single or multiple columns
# Here we are sorting based on second and first columns inside tuple in reverse order
from operator import itemgetter
student_objects = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
l1 = sorted(student_objects, key=itemgetter(2), reverse=True)
print(l1)
# [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
l2 = sorted(student_objects, key=itemgetter(1,0), reverse=True)
print(l2)
# [('jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]

#######################################################################################################################

'''
sort method:

Its syntax is: list.sort(reverse=True|False, key=myFunc)
    1. sort() function is very similar to sorted() but unlike sorted it returns nothing and makes changes to the original sequence
    2. Moreover, sort() is a method of list class and can only be used with lists. 
    3. to sort reverse order, pass reverse = True to the sort() method 

Key points
    1. The sort() function in Python uses an algorithm called Timsort, which is a hybrid sorting algorithm 
    derived from merge sort and insertion sort  
'''

# sort - List of Integers
numbers = [1, 3, 4, 2]
numbers.sort()
print(numbers)
# [1, 2, 3, 4]

# sort - Floating point numbers
decimal_number = [2.01, 2.00, 3.67, 3.28, 1.68]
decimal_number.sort() 
print(decimal_number)
# [1.68, 2.0, 2.01, 3.28, 3.67]

# sort - strings
words = ["Geeks", "For", "Geeks"]
words.sort()
print(words)
# ['For', 'Geeks', 'Geeks']

# sort - sort based on second element in ascending order
list1 = [(1, 2), (3, 3), (1, 1)]
list1.sort(key=lambda x:x[1])
print(list1)
# [(1, 1), (1, 2), (3, 3)]

# sort - sort based on second element in descending order
list1 = [(1, 2), (3, 3), (1, 1)]
list1.sort(key=lambda x:x[1])
print(list1)
# [(3, 3), (1, 2), (1, 1)]

# sort - based on single or multiple columns
from operator import itemgetter
student_objects = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
student_objects.sort(key=itemgetter(0,2))
print(student_objects)
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

#######################################################################################################################

