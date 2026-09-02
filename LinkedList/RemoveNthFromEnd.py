# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Fast and Slow Pointer
        # 0 1 2 3 4

        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next

        while fast.next != None:
            slow = slow.next
            fast = fast.next

        newNext = slow.next.next
        slow.next = newNext

        return dummy.next
