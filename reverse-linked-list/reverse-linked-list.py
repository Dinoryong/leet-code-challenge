# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None ):
            
            # base case
            if not node:
                return prev
            
            # recursive         
            next, node.next = node.next, prev
            return reverse(next, node) 
        
        return reverse(head)