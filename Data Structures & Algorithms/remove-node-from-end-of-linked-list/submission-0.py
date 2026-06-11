# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Get SIZE
        node = head
        size = 0
        while node != None:
            node = node.next
            size += 1
        
        n_index = size - n
        if n_index == 0:
            return head.next
        
        # Remove nth node
        counter = 0
        bottom = head
        while counter != n_index - 1:
            bottom = bottom.next
            counter += 1
        
        removed_node = bottom.next
        top = removed_node.next
        bottom.next = top
        return head
        

        
