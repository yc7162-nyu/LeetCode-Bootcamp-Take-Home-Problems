# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 2 pointers, n nodes apart

        dummy = ListNode()

        dummy.next = head

        l = dummy
        r = dummy

        # move r ptr n nodes ahead
        for i in range(n):
            r = r.next
        
        while r.next != None:
            r = r.next
            l = l.next
        
        l.next = l.next.next

        return dummy.next