'''
Let say we have list, sort it in ascending and descending order
'''
l = [4,3,6,3,7,5]
l.sort()
print("Ascending order: ", l)
l.sort(reverse=True)
print("Descending order", l)


'''
Let's say we have tuple, sort in asc and desc
'''

t = (4,3,2,1,5,7)
t1 = sorted(t)
t2 = sorted(t, reverse=True)
print("Ascending order: ", t1)
print("Descending order", t2)

'''
Lets say we have dictionary, which as list of values, we need to sort based on key and based on one of the list value
'''

d = {"C": [2, 'CC'], "A": [1,'AA'], "B": [3, 'CC']}

d_key_sort = sorted(d)
print("Only return keys in sorting order: ", d_key_sort)

d_key_sort_rev = sorted(d, reverse=True)
print("Only return keys in desc sorting order: ", d_key_sort_rev)

d_value_sort = sorted(d.items(), key = lambda x: x[1][0])
print("Sort based on dict value in asc: ", d_value_sort)

d_value_sort_desc = sorted(d.items(), key = lambda x: x[1][0], reverse=True)
print("Sort based on dict value in desc: ", d_value_sort_desc)


'''
Let's say we have nested list, sort based on nested value
'''

l = [[3,5], [5,3], [0,1]]

l_sort = sorted(l, key = lambda x: x[1])
print("Nested list sorted based on nested value", l_sort)