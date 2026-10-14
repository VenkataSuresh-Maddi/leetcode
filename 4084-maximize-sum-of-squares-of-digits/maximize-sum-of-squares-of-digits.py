class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        cur = ""
        temp = sum 
        res = 0
        while num>0:
            cur = cur + str(min(9,sum))
            if sum >= 9:
                sum = sum - 9 
            else:
                sum = sum - sum 
            num -= 1
        for x in cur:
            res += int(x)
        return cur if res == temp else ""
        