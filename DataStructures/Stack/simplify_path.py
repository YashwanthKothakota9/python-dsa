# Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.

# 1. 
#    Input: "/a//b////c/d//././/.."
#    Output: "/a/b/c"
   
# 2. 
#    Input: "/../"
#    Output: "/"

# 3. 
#    Input: "/home//foo/"
#    Output: "/home/foo"

# Split the input path by the "/" character into an array of components.

# Initialize an empty stack.

# For each component in the array:

# If the component is "..", pop the top of the stack (if it's not already empty).
# Else if the component is "." or an empty string, do nothing.
# Else, push the component into the stack as a new directory.
# Finally, combine the components in the stack into a string, separated by the "/" character. Add a "/" at the start to denote an absolute path.

class Solution:
    def simplifyPath(self,path):
        stack = []
        for p in path.split('/'):
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/'+'/'.join(stack)
    
def main():
    sol = Solution();
    print(sol.simplifyPath("/a//b////c/d//././/..")) # Expected output: "/a/b/c"
    print(sol.simplifyPath("/../")) # Expected output: "/"
    print(sol.simplifyPath("/home//foo/")) # Expected output: "/home/foo"

if __name__ == '__main__':
    main()