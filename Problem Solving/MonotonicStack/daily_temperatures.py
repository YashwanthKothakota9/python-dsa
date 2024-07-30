# Given an array of integers temperatures representing daily temperatures, your task is to calculate how many days you have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

# Examples

# Input: temperatures = [70, 73, 75, 71, 69, 72, 76, 73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
# Explanation: The first day's temperature is 70 and the next day's temperature is 73 which is warmer. So for the first day, you only have to wait for 1 day to get a warmer temperature. Hence, the first element in the result array is 1. The same process is followed for the rest of the days.
# Input: temperatures = [73, 72, 71, 70]
# Output: [0, 0, 0, 0]
# Explanation: As we can see, the temperature is decreasing every day. So, there is no future day with a warmer temperature. Hence, all the elements in the result array are 0.


# This problem is quite similar to 'Next Greater Element'. We can use a monotonically increasing stack to find the next higher temperature.

# We will use a stack to store the indices of the temperatures array. We iterate over the array, and for each temperature, we check whether the current temperature is greater than the temperature at the index on the top of the stack. If it is, we update the corresponding position in the result array and pop the index from the stack.


class Solution:
    def dailyTemperatures(self, temps):
        stack = []
        res = [0]*len(temps)
        for i in range(len(temps)):
            # While the stack is not empty and the current temperature is higher
            # than the temperature at the index stored at the top of the stack:
            while stack and temps[i] > temps[stack[-1]]:
                idx = stack.pop() # Pop the top index from the stack.
                res[idx] = i - idx # Calculate the number of days until warmer temperature.
            stack.append(i) # Push the current index onto the stack.
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([70, 73, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(solution.dailyTemperatures([73, 72, 71, 70])) # Output: [0, 0, 0, 0]
    print(solution.dailyTemperatures([70, 71, 72, 73])) # Output: [1, 1, 1, 0]
    

# The time complexity of the algorithm is O(N), where N is the size of the temperatures array, since we process each temperature once. The space complexity is also O(N), where N is the size of the temperatures array, due to the extra space used by the stack and the output list.