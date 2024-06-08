'''
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Input:
N = 4
Petrol = 4 6 7 4
Distance = 6 5 3 5
Output: 1
Explanation: There are 4 petrol pumps with amount of petrol and distance to next petrol pump value pairs as {4, 6}, {6, 5}, {7, 3} and {4, 5}. The first point from where truck can make a circular tour is 2nd petrol pump. Output in this case is 1 (index of 2nd petrol pump).

Your Task:
Your task is to complete the function tour() which takes the required data as inputs and returns an integer denoting a point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity). If there exists multiple such starting points, then the function must return the first one out of those. (return -1 otherwise)

Expected Time Complexity: O(N)
Expected Auxiliary Space : O(1)

lis[][0]:Petrol
lis[][1]:Distance
'''

# Solution -1 First approach 
'''
2 pointer approach
Algo steps:
    1. We need to keep track of running sum of petrol & distance till current index
    2. Init curr_petrol = 0, start=0, Counter c is use to assign start only once as starting index. back_petrol_need = 0 and back_distance=0
    3. Check current petrol available > distance we need to cover by checking (curr_petrol+lis[i][0]) > lis[i][1], if yes minus distance from curr_petrol and if c==0 then assign current index as starting index and c=1. Else assign running_sum_petrol_need to back_petrol_need & running_sum_distance to back_distance
    4. At last check curr_petrol + back_petrol_need >= back_distance if true return start index else return -1 as not possible

TC = O(N)
SC = O(1)
'''
class Solution:
    def tour(self,lis, n):
        back_petrol_need = 0
        back_distance = 0
        curr_petrol = 0
        start = 0
        c = 0
        running_sum_petrol_need = 0
        running_sum_distance = 0
        for i in range(n):
            curr_petrol += lis[i][0]
            running_sum_petrol_need += lis[i][0]
            running_sum_distance += lis[i][1]
            if curr_petrol >= lis[i][1]:
                curr_petrol -= lis[i][1]
                if c == 0:
                    start = i
                    c = 1
            else:
                back_petrol_need = running_sum_petrol_need
                back_distance = running_sum_distance
                curr_petrol = 0
                c = 0
        if curr_petrol + back_petrol_need >= back_distance:
            return start
        else:
            return -1