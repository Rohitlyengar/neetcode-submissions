"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        index = { None : None }

        curr = head

        while curr:
            index[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            node = index[curr]
            node.next = index[curr.next]
            node.random = index[curr.random]
            curr = curr.next
        
        return index[head]
