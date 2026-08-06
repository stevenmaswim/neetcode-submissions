# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = head
        slow = dummy
        count = n
        while fast and count > 0: 
            fast = fast.next
            count -= 1
        while fast:
            fast = fast.next         
            slow = slow.next
        slow.next = slow.next.next 
        return dummy.next
            