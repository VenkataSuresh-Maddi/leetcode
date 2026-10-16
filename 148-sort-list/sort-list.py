# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dup = ListNode()
        d1 = dup 
        data = []
        temp = head
        while temp:
            heapq.heappush(data,[temp.val,temp])
            temp = temp.next
        while data:
            dup.next = heapq.heappop(data)[1]
            dup = dup.next
        dup.next = None
        return d1.next
        