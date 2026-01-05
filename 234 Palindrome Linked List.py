# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find Middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse from Middle
        rev = None
        while slow:
            next = slow.next
            slow.next = rev
            rev = slow
            slow = next
       
        # Compare
        while head and rev:
            if head.val != rev.val:
                return False
            head = head.next
            rev = rev.next
        return True