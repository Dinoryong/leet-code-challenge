"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = new = Node(-1)
        cur = head
        old_new = {}

        while cur:
            new.next = Node(cur.val)
            old_new[cur] = new.next
            cur = cur.next
            new = new.next
            
        cur = head
        new = dummy.next
        
        while cur:
            if cur.random:
                new.random = old_new[cur.random]
            cur = cur.next
            new = new.next
        return dummy.next