# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input: [3, 2, 6, 5, 0, 3]
# Expected Output: 4
# Justification: Buy the stock on day 2 (price = 2) and sell it on day 3 (price = 6). Profit = 6 - 2 = 4.
# Input: [8, 6, 5, 2, 1]
# Expected Output: 0
# Justification: Prices are continuously dropping, so no profit can be made.
# Input: [1, 2]
# Expected Output: 1
# Justification: Buy on day 1 (price = 1) and sell on day 2 (price = 2). Profit = 2 - 1 = 1.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# Solution
# To solve this problem, we iterate through the list of stock prices to find the maximum profit that can be made by buying and selling once. The approach involves keeping track of the lowest price seen so far and calculating the potential profit if the stock were sold at the current price. As we continue to iterate through the prices, we consistently update the minimum price and the maximum profit observed. By the end of the loop, we have determined the highest possible profit that can be achieved from a single buy-sell transaction, ensuring an efficient solution with linear time complexity.

# Complexity Analysis
# Time Complexity: O(n), where n is the number of days. This is because the algorithm iterates through the list of prices once, performing constant-time operations for each price.
# Space Complexity: O(1), as it uses a constant amount of extra space (two variables to keep track of minPrice and maxProfit).


class Solution:
    def maxProfit(self, prices):
        minPrice, maxProfit = float('inf'), 0
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price-minPrice)
        return maxProfit


solution = Solution()
example1 = [3, 2, 6, 5, 0, 3]
example2 = [8, 6, 5, 2, 1]
example3 = [1, 2]
print(solution.maxProfit(example1))  # Output: 4
print(solution.maxProfit(example2))  # Output: 0
print(solution.maxProfit(example3))  # Output: 1
