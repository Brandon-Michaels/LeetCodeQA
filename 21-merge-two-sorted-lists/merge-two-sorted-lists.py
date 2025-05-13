# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach
        # traverse arrays if val left <= right add left, else add right
        # Time-Complexity: O(n + m), where n is size LL1, m size of LL2
        # Space-Complexity: O(1)

        head = node = ListNode()

        while (list1 is not None and list2 is not None):
            if (list1.val <= list2.val):
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        while (list1 is not None):
            node.next = list1
            list1 = list1.next
            node = node.next

        while (list2 is not None):
            node.next = list2
            list2 = list2.next
            node = node.next
        
        return head.next