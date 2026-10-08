class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        ans = ""
        count = 0
        for i in range(len(s)):
            if count == 0:
                count+=1
            elif s[i] == '(' and count > 0:
                ans = ans + s[i]
                count += 1 
            elif s[i] == ')'and count == 1:
                count -= 1
            elif s[i] == ')':
                ans = ans + s[i]
                count -= 1
        return ans