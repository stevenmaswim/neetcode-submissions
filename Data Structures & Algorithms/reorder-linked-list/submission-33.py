# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        while first.next and first.next.next:
            cur = first
            second = first.next
            while cur.next:
                second_last = cur
                cur = cur.next
            cur.next = second
            first.next = cur
            first = second
            second_last.next = None