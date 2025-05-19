# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Intuition:
        # traverse LL to find length
        # n - len(LL) is node to remove
        # Time-Complexity: O(n), where n is the size of LL
        # Space-Complexity: O(1)

        temp_curr = head
        length = 0
        while (temp_curr):
            temp_curr = temp_curr.next
            length += 1
        
        removeIdx= length - n
        # edge case
        if removeIdx == 0:
            return head.next

        
        curr = head
        for i in range(length - 1):
            if (i + 1) == removeIdx:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head