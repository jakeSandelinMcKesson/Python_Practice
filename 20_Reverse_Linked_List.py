# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            child = curr.next
            curr.next = prev
            prev = curr
            curr = child
        return prev # can't return the curr at the end because that will actually be None eventually. 