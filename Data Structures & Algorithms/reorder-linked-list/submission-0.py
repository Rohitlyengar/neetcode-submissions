# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        newHead = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return newHead
    

    def middle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        return second
    

    def reorder(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> None:
        while head2:
            tmp1, tmp2 = head1.next, head2.next
            head1.next = head2
            head2.next = tmp1

            head1, head2 = tmp1, tmp2 


    def reorderList(self, head: Optional[ListNode]) -> None:
        self.reorder(head, self.reverse(self.middle(head)))

        