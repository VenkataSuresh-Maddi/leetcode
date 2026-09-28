class Solution(object):

    def getIntersectionNode(self, headA, headB):
        visited = set()

        curA = headA
        while curA:
            visited.add(curA)
            curA = curA.next

        curB = headB
        while curB:
            if curB in visited:
                return curB
            curB = curB.next

        return None