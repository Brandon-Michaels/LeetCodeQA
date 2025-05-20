# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Intuition
        # Sum numbers under 10 as normal
        # else use overflow by using modulo and integer division
        # Time-Complexity: O(m + n), where n is size of l1 and m is size of l2
        # Space-Complexity: O(max(m + n)), where new LL is max of either l1 or l2

        temp = ListNode()
        curr = temp
        overflow = 0
        res = 0
        v1 = 0
        v2 = 0

        while (l1 or l2 or overflow):
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
                
            res = overflow + v1 + v2
            overflow = res // 10
            res = res % 10
            
            tempNode = ListNode(res)
            curr.next = tempNode
            curr = curr.next
        
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temp.next