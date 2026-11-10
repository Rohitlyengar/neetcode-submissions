# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head

        while temp and count < k:
            temp = temp.next
            count += 1
        
        if count < k:
            return head
        
        newHead = self.reverseList(head, temp)
        head.next = self.reverseKGroup(temp, k)
        
        return newHead


    def reverseList(self, start: Optional[ListNode], end: Optional[ListNode]) -> Optional[ListNode]:
        if start is None or start.next is end:
            return start
        
        newHead = self.reverseList(start.next, end)
        start.next.next = start
        start.next = None

        return newHead
