'''
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Input: s = "100[code]"
Ouput: 100 times code
'''

# Solution-1: Stack approach
'''
Algorithm:
    1. Maintain stack and keep on adding ele if not ']'
    2. If ele in '[',
        2.1 create 2 temp lists to track count number and elements
        2.2 First pop all char element till '[' and add it to temp list
        2.3 Next pop all numeric element till next char and add it to temp list
        2.4 convert temp list to string and generate count times string
        2.5 Add it to main stack
    3. return stack by converting it into string

Time Complexity = O(N*M)
Space Complexity = O(N)
'''
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ele in s:
            if ele != ']':
                stack.append(ele)
            elif ele == ']':
                repeat_count = []
                temp_ele_stack = []
                while True:
                    if len(stack) > 0:
                        if stack[-1] != '[':
                            temp_ele = stack.pop()
                            temp_ele_stack.insert(0, temp_ele)
                        elif stack[-1] == '[':
                            stack.pop()
                            break
                    else:
                        break
                while True:       
                        if len(stack) > 0:
                            if stack[-1].isnumeric():
                                temp_ele = stack.pop()
                                repeat_count.insert(0,temp_ele)
                            else:
                                break
                        else:
                            break
                n_times = "".join(temp_ele_stack) * int("".join(repeat_count))
                stack.append(n_times)
        return "".join(stack)