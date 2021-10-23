# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # sortedList에 처음 넣는 값을 조건문으로 처리하지 않기 위해
        result = sortedList = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                sortedList.next = l1
                l1 = l1.next
            else:
                sortedList.next = l2
                l2 = l2.next
            sortedList = sortedList.next
        sortedList.next = l1 or l2
        return result.next
