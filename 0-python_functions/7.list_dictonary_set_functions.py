'''
How to delete (k, v) pair from dict
'''

d = {"A":1, "B": 2}
d.pop('A')

'''
How to sort dict based on key and value
'''

d = {"A":1, "B": 2}

sorted_key = sorted(d.items(), key=lambda x: x[0]) # sorted by key

sorted_value = sorted(d.items(), key=lambda x: x[1]) # sorted by value

'''
How to sort dict by one one of value of list
'''

d = {"A":[11, 'O'], "B": [2, 'S']}

sorted_by_list_value = sorted(d.items(), key=lambda x: x[1][0])


d.items() # returns (k, v)
d.keys()  # returns keys
d.values() # return values
d.pop(key) # delete key from dict