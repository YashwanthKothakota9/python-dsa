# Given an integer array and an integer k, design an algorithm to find the maximum for each and every contiguous subarray of size k.

# Examples:

# Input: array = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
# Output: [3, 3, 4, 5, 5, 5, 6]
# Description: Here, subarray 1,2,3 has maximum 3, 2,3,1 has maximum 3, 3,1,4 has maximum 4, 1,4,5 has maximum 5, 4,5,2 has maximum 5, 5,2,3 has maximum 5, and 2,3,6 has maximum 6.

# Input: array = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], k = 4
# Output: [10, 10, 10, 15, 15, 90, 90]
# Description: Here, the maximum of each subarray of size 4 are 10, 10, 10, 15, 15, 90, 90 respectively.

# Input: array = [1,2,3,4,5], k = 3
# Output: [3, 4, 5]
# Description: Here, the maximum of each subarray of size 3 are 3, 4, 5 respectively.

from collections import deque

class Solution:
    def printMax(self,arr,k):
        dq = deque()
        result = []
        n = len(arr)
        for i in range(min(k,n)):
            # For every element, the previous smaller elements are useless, so remove them from dq
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            dq.append(i)
        print("First K: ",dq)
        for i in range(k,n):
            result.append(arr[dq[0]])
            print("result: ",result)
            # Remove the elements which are out of this window
            while dq and dq[0] <= i-k:
                dq.popleft()
            
            print("1.",dq)
            # Remove all elements smaller than the currently being added element
            # (Remove useless elements)
            while dq and arr[i] >= arr[dq[-1]]:
                dq.pop()
            print("2.",dq)
            dq.append(i)
            print("3.",dq)
        result.append(arr[dq[0]])
        return result
    
sol = Solution()
arr = [9, 7, 2, 4, 6, 8, 2, 11, 1]
k = 3
result = sol.printMax(arr, k)

# Print the result
print(result)