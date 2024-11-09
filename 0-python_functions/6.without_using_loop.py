'''
Write a function to find 2nd occurance index of element in list with using loop or iterables

l = [1,2,3,4,5,2,9]

output: 6
'''

def second_occ(l, ele):
    first_occ = l.index(ele)
    second_occ = l[first_occ+1:].index(ele)
    return second_occ