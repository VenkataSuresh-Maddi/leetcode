class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        cur = ""
        res = []
        if sum > 9*num:
            return ""
        for i in range(num):
            if sum > 9:
                res.append('9')
                sum = sum - 9
            else:
                res.append(str(sum))
                sum = sum - sum 
        return "".join(res)
            
            