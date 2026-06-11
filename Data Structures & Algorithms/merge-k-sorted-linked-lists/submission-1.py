# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Find min node from all lists
        min_val = float('inf')
        min_node = None
        for head in lists:
            if head != None and min_val >= head.val:
                min_val = head.val
                min_node = head
        if min_node == None:
            return None
        chosen = min_node # List to modify in-place
        end_of_sorted = chosen
        start_of_unsorted = end_of_sorted.next
        end_of_sorted.next = None

        while True:
            min_val = float('inf')
            min_node = None
            min_index = 0
            for i in range(len(lists)):
                ll = lists[i]
                if ll == chosen:
                    if start_of_unsorted != None and min_val >= start_of_unsorted.val:
                        min_val = start_of_unsorted.val
                        min_node = start_of_unsorted
                else:
                    if ll != None and min_val >= ll.val:
                        min_val = ll.val
                        min_node = ll
                        min_index = i
            if min_node == None:
                break
            if min_node == start_of_unsorted:
                start_of_unsorted = start_of_unsorted.next
            else:
                ll = lists[min_index]
                lists[min_index] = ll.next
            end_of_sorted.next = min_node
            end_of_sorted = min_node
            end_of_sorted.next = None
        return chosen
        
            
                



            
