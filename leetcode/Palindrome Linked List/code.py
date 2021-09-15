# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        result = []
        
        while head != None:
            value = head.val
            head = head.next
            result.append(value)
        
        if result == result[::-1]:
            return True
        return False