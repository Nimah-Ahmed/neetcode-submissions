# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find size of list
        size = 0
        node = head
        while node != None:
            node = node.next
            size += 1
        

        # If ODD
        if size % 2 != 0:
            end_of_left = size // 2
        else: # If EVEN
            end_of_left = size // 2 - 1

        # Reverse the right part of the list
        # find the beginning right node
        b = head
        counter = 0
        while counter != end_of_left + 1:
            if counter == end_of_left:
                imp = b
            b = b.next
            counter += 1
        
        imp.next = None
        
        # reverse
        a = None
        right_node = None
        while b != None:
            if b.next == None:
                right_node = b
            c = b.next
            b.next = a
            a = b
            b = c
        
        # Insertion
        left_node = head
        while right_node != None:
            print("hello")
            top = left_node.next
            next_right_node = right_node.next
            left_node.next = right_node
            right_node.next = top
            right_node = next_right_node
            left_node = top

        



        


        

        
        

        




