# To assign maximum integer value
import sys
val = sys.maxsize

# to loop through integer > 10 or string of characters
value = 10  # or value = "ABC" 
for i in str(value):
    print(i)


# to combine 2 lists
l1 = [1,2,3,4]
l2 = [5,6,7,8]
# You can use *to unpack or use + to concat 2 lists
res = [*l1, *l2]
res = l1 + l2
print(res) # output - [1,2,3,4,5,6,7,8]


# dictionary vs defaultdict
'''
Both are (k,v) pairs only
If key not found in dictionary, it through key error.
If key not found in defaultdict, it doesn't through key error. Instead it returns default value  
Usecase:
    dict = if you upfront know what key you store and access
    defaultdict = If you don't know upfront what key you store and access 
'''
from collections import defaultdict

dd = defaultdict(int)
dd['a']=1
dd['b']=2

print(dd['a'], dd['b'],dd['c'])
# Output : 1  2  0
# returns 0 for dd['c'], because we set default to int while initializing defaultdict

# OrderedDict
'''
It maintains the order in which key are added to dict.
'''
from collections import orderedDict

od = orderedDict()
od['a']=1
od['b']=2

for k, v in od.items():
    print(k,v)

# Output:
# a 1
# b 2


# Heap queue - priority queue
https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/