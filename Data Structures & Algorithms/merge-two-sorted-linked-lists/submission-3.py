# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Algorithm --> O(n) time, O(1) space:
            1. Initialization: 
                a. list1_node = list1
                b. list2_node = list2
                c. end_of_sorted = Listnode()
            2. Maintenance:
                have: end_of_sorted, list2_node, list1_node
                a. At iteration i:
                    if list1_node value < list2_node value:
                        # shifts the list1 pointer accordingly
                        node_to_insert = list1_node
                        list1_node = list1_node.next
                        # insert the node
                        end_of_sorted.next = node_to_insert
                        node_to_insert.next = list_2_node
                        # make sure all variables fit to their description
                        end_of_sorted = node_to_insert
                    else: # list1_node value > list2_node value
                        # shift list2 pointer accordingly
                        list2_node = list2_node.next
                        # variables fit their description
                        end_of_sorted = end_of_sorted.next
            3. Termination: 
                a. list1_node == None or list2_node == None
                b. list1_node == None: do nothing
                c. list2_node == None:
                    end_of_sorted.next = list_1_node
        """
        
        list1_node = list1
        if list1_node == None:
            return list2
        list2_node = list2
        end_of_sorted = ListNode()
        output_head = end_of_sorted
        while list1_node != None and list2_node != None:
            if list1_node.val <= list2_node.val:
                # shifts the list1 pointer accordingly
                node_to_insert = list1_node
                list1_node = list1_node.next
                # insert the node
                end_of_sorted.next = node_to_insert
                node_to_insert.next = list2_node
                # make sure all variables fit to their description
                end_of_sorted = node_to_insert
            else: # list1_node value > list2_node value
                node_to_insert = list2_node
                list2_node = list2_node.next
                end_of_sorted.next = node_to_insert
                node_to_insert.next = list2_node
                end_of_sorted = node_to_insert

        if list2_node == None:
            end_of_sorted.next = list1_node
        return output_head.next
        

            



                



        