'''
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = []
Output: []

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Solution-1: Iterative approach
'''
Time complexity = O(N)
Space complexity = O(1)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

