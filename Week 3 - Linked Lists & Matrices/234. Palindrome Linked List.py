# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
    
        f = head
        s = head

        # Even number of nodes, s at mid when f at second last node
        # Odd number of nodes, s at mid when f at last node

        while f.next != None and f.next.next != None:
            f = f.next.next
            s = s.next
        
        second_half_start = s

        head2 = self.reverseLL(second_half_start.next)
        second_half_start.next = None

        c1 = head
        c2 = head2

        while c1 != c2 and c2 != None:
            if c1.val != c2.val:
                return False
            
            c1 = c1.next
            c2 = c2.next

        return True
    
    # Reverses LL starting at head and returns the new head
    def reverseLL(self, head):
        prev = None
        curr = head

        while curr != None:
            n = curr.next
            curr.next = prev

            prev = curr
            curr = n
        
        return prev
            


'''
    1 2 3 4 5 6
        s.  f

    1 2 3 4 5
        s     f

    <1 <-2 3->4->
          pc. n
'''

