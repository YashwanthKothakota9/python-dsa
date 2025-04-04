# Given an integer N, generate all binary numbers from 1 to N and return them as a list of strings.

# Examples:

# Input: N = 2
# Output: ["1", "10"]
# Explanation: The binary representation of 1 is "1", and the binary representation of 2 is "10".

# Input: N = 3
# Output: ["1", "10", "11"]
# Explanation: The binary representation of 1 is "1", the binary representation of 2 is "10", and the binary representation of 3 is "11".

# Input: N = 5
# Output: ["1", "10", "11", "100", "101"]
# Explanation: These are the binary representations of the numbers from 1 to 5.

from queue import Queue

class Solution:
    def generate_binary_numbers(self,n):
        q = Queue()
        q.put("1")
        res = []
        while n > 0:
            res.append(q.get())
            s1 = res[-1] + "0"
            s2 = res[-1] + "1"
            q.put(s1)
            q.put(s2)
            n -= 1
        return res


sol = Solution()
print(sol.generate_binary_numbers(2))
print(sol.generate_binary_numbers(3))
print(sol.generate_binary_numbers(15))
