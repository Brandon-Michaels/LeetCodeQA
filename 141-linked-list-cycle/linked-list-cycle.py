# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Intuition
        # fast, slow pointer
        # Time-complexity: O(n), n is size of LL
        # Space-complexity: O(1)

        fast = head
        slow = head

        while (fast is not None):
            if (fast.next is None):
                return False
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                return True

        return False