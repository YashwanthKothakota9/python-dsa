# Problem Statement
# Given an absolute file path in a Unix-style file system, simplify it by converting ".." to the previous directory and removing any "." or multiple slashes. The resulting string should represent the shortest absolute path.

# Examples
# Example 1
# Input: path = "/a//b////c/d//././/.."
# Expected Output: "/a/b/c"
# Explanation:
# Convert multiple slashes (//) into single slashes (/).
# "." refers to the current directory and is ignored.
# ".." moves up one directory, so "d" is removed.
# The simplified path is "/a/b/c".
# Example 2
# Input: path = "/../"
# Expected Output: "/"
# Explanation:
# ".." moves up one directory, but we are already at the root ("/"), so nothing happens.
# The final simplified path remains "/".
# Example 3
# Input: path = "/home//foo/"
# Expected Output: "/home/foo"
# Explanation:
# Convert multiple slashes (//) into single slashes (/).
# The final simplified path is "/home/foo".
# Constraints:

# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.


# Solution
# To simplify the path, we'll use a stack to track the directories we're currently in. We'll split the input path into components by the "/" character, then process each component one by one. If a component is "..", we go to the previous directory by popping the top of the stack. If a component is "." or an empty string, we do nothing. Otherwise, we push the component into the stack as a new directory.


# Time Complexity
# Splitting the path: The input string path is split using / as the delimiter, which takes  O(N) time, where N is the length of the input string path. This creates an array of strings representing the components of the path.

# Processing the components: The algorithm processes each component of the path array. For each component, it either pushes it onto the stack, pops an element from the stack, or skips the component if it is . or empty. Since each component is processed at most once, this takes O(N) time in total.

# Building the result: After processing all components, the algorithm reconstructs the simplified path by concatenating the elements in the stack. This also takes O(N) time.

# Overall time complexity: O(N), where N is the length of the input string path.

# Space Complexity
# Stack space: The stack stores the components of the simplified path. In the worst case, the stack contains all components of the path, which requires O(N) space.

# Result string space: The result string is used to store the final result which also takes  O(N) space, as it holds the result of the same size as the input string (in the worst case).

# Overall space complexity: O(N).


class Solution:
    def simplify_path(self, path):
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != ".":
                stack.append(p)

        return "/" + "/".join(stack)


sol = Solution()
print(sol.simplify_path("/a//b////c/d//././/.."))  # Expected output: "/a/b/c"
print(sol.simplify_path("/../"))  # Expected output: "/"
print(sol.simplify_path("/home//foo/"))  # Expected output: "/home/foo"
