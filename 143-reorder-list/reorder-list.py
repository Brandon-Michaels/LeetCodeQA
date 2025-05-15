# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Intuition
        # Reverse back-half of LL, two-ptr approach
        # L -> R, R -> L.next, L -> R.next (L ++, R --)
        # Time-Complexity: O(n), where n is len(LL)
        # Space-Complexity: O(1)

        fast, slow = head.next, head

        # get slow to half-way point
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        # reverse back-half of LL
        prev = None
        curr = slow.next
        slow.next = None
        while (curr):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # re-order LL
        # prev points to back head
        left = head
        right = prev
        while (right):
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next
            right = right_next
            left = left_next