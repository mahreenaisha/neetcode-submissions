# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # floyd's tortoise and hare
        # did not understand the mathematical explanation given by neetcode that it is inevitable for the fast pointer to reach the slow pointer - revisit this later
        # tc = o(n), sc - 0(1)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
        