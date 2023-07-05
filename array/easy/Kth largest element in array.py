'''
Given an array and value K

return kth largest element from array

arr = [1,2,3,1,3,4]
k = 2
output: 3

arr = [1,1,1,2,3,5,7,7,5]
k = 2
output: 5
'''

def largest(arr, k):
    s = set(arr)
    l = list(s)
    l.sort()
    return l[-k]


# Kth smallest

def smallest(arr, k):
    s = set(arr)
    l = list(s)
    l.sort(reverse=True)
    return l[-k]