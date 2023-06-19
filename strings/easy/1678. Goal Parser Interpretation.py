'''
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
 The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
 The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
'''

class Solution:
    def interpret(self, command: str) -> str:
        goal_parser = ""
        str_len = len(command)-1
        index = 0
        while index <= str_len:
            if command[index] == 'G':
                goal_parser = goal_parser + 'G'
                index = index + 1
            elif command[index:index+2] == '()':
                goal_parser = goal_parser + 'o'
                index = index + 2
            elif command[index:index+4] == '(al)':
                goal_parser = goal_parser + 'al'
                index = index + 4
        return goal_parser