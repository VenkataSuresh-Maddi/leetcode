class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = deque()
        hm = {}
        res = []
        for i in range(len(nums2)):
            if len(stack) == 0 or stack[-1]>nums2[i]:
                stack.append(nums2[i])
            else:
                while len(stack) > 0 and stack[-1] < nums2[i]:
                    hm[stack.pop()] = nums2[i]
                stack.append(nums2[i])
        for i in range(len(nums1)):
            if nums1[i] in hm:
                res.append(hm[nums1[i]])
            else:
                res.append(-1)
        return res 