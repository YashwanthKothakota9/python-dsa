# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:

# Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# You can start with any tree, but you can’t skip a tree once you have started.
# You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.

# Example 1:

# Input: arr=['A', 'B', 'C', 'A', 'C']  
# Output: 3  
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:

# Input: arr = ['A', 'B', 'C', 'B', 'B', 'C']  
# Output: 5  
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']


# To solve this problem, we use a sliding window approach. This technique is effective for problems involving contiguous subarrays or sublists. The sliding window approach allows us to maintain a window of elements that meet a certain condition—in this case, having no more than two types of fruits. We expand the window by adding elements from the right and contract it from the left when the condition is violated. This approach ensures we check all possible subarrays without starting from each element repeatedly, making it efficient.

# This method works well because it continuously adjusts the window size based on the elements it encounters. By using a dictionary to keep track of the fruit counts within the window, we can efficiently manage and adjust the window size to find the maximum length subarray that satisfies the condition. The efficiency comes from the fact that each element is processed at most twice, once when added and once when removed from the window.

# Time Complexity

# The above algorithm’s time complexity will be O(N) , where ‘N’ is the number of characters in the input array. The outer 'for' loop runs for all characters, and the inner 'while' loop processes each character only once; therefore, the time complexity of the algorithm will be O(N+N) , which is asymptotically equivalent to O(N) .

# Space Complexity

# The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.



class Solution:
    def findLength(self, fruits):
        window_start = 0
        max_length = 0
        fruit_freq = {}
        
        # try to extend the range [window_start, window_end]
        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]
            if right_fruit not in fruit_freq:
                fruit_freq[right_fruit] = 0
            fruit_freq[right_fruit] += 1
            
            # shrink the sliding window, until we are left with '2' fruits in the fruit
            # frequency dictionary
            while len(fruit_freq) > 2:
                left_fruit = fruits[window_start]
                fruit_freq[left_fruit] -= 1
                if fruit_freq[left_fruit] == 0:
                    del fruit_freq[left_fruit]
                window_start += 1
            max_length = max(max_length, window_end - window_start + 1)
        return max_length


def main():
    sol = Solution()
    print("Maximum number of fruits: "
          + str(sol.findLength(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: "
          + str(sol.findLength(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
