# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        dummy = ListNode()
        for head in lists:
            current = head
            while current: 
                array.append(current.val)
                current = current.next
        heapq.heapify(array)
        curr = dummy
        while array:
            curr.next = ListNode(heapq.heappop(array))
            curr = curr.next
        return dummy.next
        