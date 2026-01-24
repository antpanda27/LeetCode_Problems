# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def listlen(listnode: ListNode) -> int:
            length = 0
            curr = listnode
            while curr:
                length += 1
                curr = curr.next
            return length

        diff = listlen(headA) - listlen(headB)
        currA, currB = headA, headB

        if diff > 0:
            while diff:
                currA = currA.next
                diff -= 1
        elif diff < 0:
            while abs(diff):
                currB = currB.next
                diff += 1
            
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None

        # seen = set()

        # curr = headA
        # while curr:
        #     seen.add(curr)
        #     curr = curr.next

        # curr = headB
        # while curr:
        #     if curr in seen:
        #         return curr
        #     curr = curr.next

        # return None