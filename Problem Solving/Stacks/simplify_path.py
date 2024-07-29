# Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.

# Examples:
# 1. 
#    Input: "/a//b////c/d//././/.."
#    Output: "/a/b/c"
   
# 2. 
#    Input: "/../"
#    Output: "/"

# 3. 
#    Input: "/home//foo/"
#    Output: "/home/foo"


class Solution:
    def simplifyPath(self, path):
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p!='.':
                stack.append(p)
        return '/'+'/'.join(stack)

sol = Solution()
print(sol.simplifyPath("/a//b////c/d//././/..")) # Expected output: "/a/b/c"
print(sol.simplifyPath("/../")) # Expected output: "/"
print(sol.simplifyPath("/home//foo/")) # Expected output: "/home/foo"

# The time complexity of the algorithm is O(n), where n is the size of the input path, since we process each character once. The space complexity is also O(n), as we store each directory in a stack.