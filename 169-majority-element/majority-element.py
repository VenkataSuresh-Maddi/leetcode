class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif nums[i] == candidate:
                count += 1
            elif nums[i] != candidate:
                count -=1
        return candidate