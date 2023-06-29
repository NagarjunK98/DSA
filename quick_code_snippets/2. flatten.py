'''
Flatten the nested list
'''
# Solution-1: Using itertools
import itertools
lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]
flatList = list(itertools.chain(*lis))
print(flatList)
# [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]

# Solution-2: using recursion

l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
output = []

def remove_Nestings(l):
	for i in l:
		if type(i) == list:
			remove_Nestings(i)
		else:
			output.append(i)

remove_Nestings(l)
print(output)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]