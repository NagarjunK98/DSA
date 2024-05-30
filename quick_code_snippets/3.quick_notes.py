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
res = [*l1, *l2]
or
res = l1 + l2
print(res) # output - [1,2,3,4,5,6,7,8]