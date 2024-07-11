from collections import deque

class Solution:
    def check_palindrome(self, s):
        # Remove all non-alphanumeric characters and convert to lowercase
        s = ''.join(filter(str.isalnum,s)).lower()
        # print(s)
        q = deque(s)
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

sol = Solution()
print(sol.check_palindrome('madam'))  # returns: True
print(sol.check_palindrome('openai'))  # returns: False
print(sol.check_palindrome('A man a plan a canal Panama'))  # returns: True
