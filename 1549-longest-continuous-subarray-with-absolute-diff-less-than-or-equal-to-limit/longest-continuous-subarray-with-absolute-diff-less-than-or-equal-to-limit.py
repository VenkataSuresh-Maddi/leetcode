class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        min_heap = []
        max_heap = []
        left = 0
        max_len = 0
        for right,num in enumerate(nums):
            heapq.heappush(min_heap,(num,right))
            heapq.heappush(max_heap,(-num,right))
            while min_heap and max_heap and -max_heap[0][0]-min_heap[0][0] > limit:
                left+=1
                while min_heap and min_heap[0][1]<left:
                    heapq.heappop(min_heap)
                while max_heap and max_heap[0][1]<left:
                    heapq.heappop(max_heap)
            max_len = max(max_len,right-left+1)
        return max_len