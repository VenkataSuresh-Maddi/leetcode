class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        queue = deque()
        ans = ""
        count = 0
        for i in range(len(s)):
            if len(queue) == 0:
                queue.append(s[i])
                count = 1
            elif s[i] == '(':
                queue.append(s[i])
                count += 1 
            elif s[i] == ')':
                queue.append(s[i])
                count -= 1
            if count == 0:
                queue.popleft()
                while len(queue) > 1:
                    ans = ans + queue.popleft()
                queue.pop()
        return ans