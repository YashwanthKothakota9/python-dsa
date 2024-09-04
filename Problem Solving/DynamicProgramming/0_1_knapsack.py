# Given two integer arrays to represent weights and profits of ‘N’ items, find a subset of these items that will give us maximum profit such that their cumulative weight is not more than a given number ‘C’, and return the maxium profit. Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

# Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

# Items: { Apple, Orange, Banana, Melon }

# Weights: { 2, 3, 1, 4 }

# Profits: { 4, 5, 3, 7 }

# Knapsack capacity: 5

# Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:

# Apple + Orange (total weight 5) => 9 profit

# Apple + Banana (total weight 3) => 7 profit

# Orange + Banana (total weight 4) => 8 profit

# Banana + Melon (total weight 5) => 10 profit

# This shows that Banana + Melon is the best combination as it gives us the maximum profit, and the total weight does not exceed the capacity.


# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.


# Basic Brute force solution
class Solution:
    def solveKnapsack(self, profits, weights, capacity):
        return self.knapsack_recursive(profits, weights, capacity, 0)
    
    def knapsack_recursive(self, profits, weights, capacity, currIndex):
        # base case
        if capacity <= 0 or currIndex >= len(profits):
            return 0
        
        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't 
        # process this
        profit1 = 0
        if weights[currIndex] <= capacity:
            profit1 = profits[currIndex] + self.knapsack_recursive(profits, weights, capacity - weights[currIndex], currIndex + 1)
        
        # recursive call after excluding the element at the currentIndex
        profit2 = self.knapsack_recursive(profits, weights, capacity, currIndex + 1)
        
        return max(profit1, profit2)


def main():
  sol = Solution()
  print(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()


# The above algorithm’s time complexity is exponential O(2^n), where ‘n’ represents the total number of items. This can also be confirmed from the above recursion tree. As we can see, we will have a total of ‘31’ recursive calls – calculated through 2^n + (2^n)-1, which is asymptotically equivalent to O(2^n).

# The space complexity is O(n). This space will be used to store the recursion stack. Since the recursive algorithm works in a depth-first fashion, which means that we can’t have more than ‘n’ recursive calls on the call stack at any time.

# ---------------------------------------------------------------

# Top-down Dynamic Programming with Memoization
# Memoization is when we store the results of all the previously solved sub-problems and return the results from memory if we encounter a problem that has already been solved.

# Since we have two changing values (capacity and currentIndex) in our recursive function knapsackRecursive(), we can use a two-dimensional array to store the results of all the solved sub-problems. As mentioned above, we need to store results for every sub-array (i.e., for every possible index ‘i’) and every possible capacity ‘c.’

class Solution1:
    def solveKnapsack(self, profits, weights, capacity):
        # create a two dimensional array for Memoization, each element is initialized to '-1'
        dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
        return self.knapsack_recursive(dp, profits, weights, capacity, 0)
    
    def knapsack_recursive(self, dp, profits, weights, capacity, currIdx):
        # base case
        if capacity <= 0 or currIdx >= len(profits):
            return 0
        
        # if we have already solved a similar problem, return the result from memory
        if dp[currIdx][capacity] != -1:
            return dp[currIdx][capacity]
        
        # recursive call after choosing the element at the currentIndex
        # if the weight of the element at currentIndex exceeds the capacity, we
        # shouldn't process this
        profit1 = 0
        if weights[currIdx] <= capacity:
            profit1 = profits[currIdx] + self.knapsack_recursive(dp, profits, weights, capacity - weights[currIdx], currIdx+1)
        
        # recursive call after excluding the element at the currentIndex
        profit2 = self.knapsack_recursive(dp, profits, weights, capacity, currIdx+1)
        
        dp[currIdx][capacity] = max(profit1, profit2)
        return dp[currIdx][capacity]

def main1():
  sol = Solution1()
  print(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
  print(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main1()

# Time and Space Complexity
# Since our memoization array dp[profits.length][capacity+1] stores the results for all subproblems, we can conclude that we will not have more than NC subproblems (where ‘N’ is the number of items and ‘C’ is the knapsack capacity). This means that our time complexity will be O(NC).

# The above algorithm will use O(NC) space for the memoization array. Other than that, we will use O(N) space for the recursion call-stack. So the total space complexity will be O(NC + N), which is asymptotically equivalent to O(N*C).

# ------------------------------------------------------------------

# Bottom-up Dynamic Programming
# Let’s try to populate our dp[][] array from the above solution by working in a bottom-up fashion. Essentially, we want to find the maximum profit for every sub-array and every possible capacity. This means that dp[i][c] will represent the maximum knapsack profit for capacity ‘c’ calculated from the first ‘i’ items.

# So, for each item at index ‘i’ (0 <= i < items.length) and capacity ‘c’ (0 <= c <= capacity), we have two options:

# Exclude the item at index ‘i.’ In this case, we will take whatever profit we get from the sub-array excluding this item => dp[i-1][c].
# Include the item at index ‘i’ if its weight is not more than the capacity. In this case, we include its profit plus whatever profit we get from the remaining capacity and from remaining items => profit[i] + dp[i-1][c-weight[i]].
# Finally, our optimal solution will be maximum of the above two values:

# dp[i][c] = max (dp[i-1][c], profit[i] + dp[i-1][c-weight[i]])

class Solution2:
    def solveKnapsack(self, profits, weights, capacity):
        n = len(profits)
        if capacity <= 0 or n==0 or len(weights)!=n:
            return 0
        
        dp = [[0 for x in range(capacity+1)]for y in range(n)]
        
        # populate the capacity = 0 columns, with '0' capacity we have '0' profit
        for i in range(0, n):
            dp[i][0] = 0
        
        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity+1):
            if weights[0] <= c:
                dp[0][c] = profits[0]
        
        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, capacity+1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i-1][c-weights[i]]
                # exclude the item
                profit2 = dp[i-1][c]
                # take maximum
                dp[i][c] = max(profit1, profit2)
        
        # maximum profit will be at the bottom-right corner.
        return dp[n-1][capacity]

def main2():
  sol = Solution2()
  print(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))


main2()

# Time and Space complexity
# The above solution has the time and space complexity of O(N*C), where ‘N’ represents total items, and ‘C’ is the maximum capacity.


# ----------------------------------------------------------------

# Let’s write a function to print the set of items included in the knapsack:


class Solution3:
    def solveKnapsack(self, profits, weights, capacity):
        n = len(profits)
        if capacity <= 0 or n==0 or len(weights)!=n:
            return 0
        
        dp = [[0 for x in range(capacity+1)]for y in range(n)]
        
        # populate the capacity = 0 columns, with '0' capacity we have '0' profit
        for i in range(0, n):
            dp[i][0] = 0
        
        # if we have only one weight, we will take it if it is not more than the capacity
        for c in range(0, capacity+1):
            if weights[0] <= c:
                dp[0][c] = profits[0]
        
        # process all sub-arrays for all the capacities
        for i in range(1, n):
            for c in range(1, capacity+1):
                profit1, profit2 = 0, 0
                # include the item, if it is not more than the capacity
                if weights[i] <= c:
                    profit1 = profits[i] + dp[i-1][c-weights[i]]
                # exclude the item
                profit2 = dp[i-1][c]
                # take maximum
                dp[i][c] = max(profit1, profit2)
        
        self.print_selected_elements(dp, weights, profits, capacity)
        # maximum profit will be at the bottom-right corner.
        return dp[n-1][capacity]
    
    def print_selected_elements(self, dp, weights, profits, capacity):
        print("Selected weights are: ", end='')
        n = len(weights)
        totalProfit = dp[n-1][capacity]
        for i in range(n-1, 0, -1):
            if totalProfit != dp[i-1][capacity]:
                print(str(weights[i])+" ", end='')
                capacity -= weights[i]
                totalProfit -= profits[i]
        if totalProfit != 0:
            print(str(weights[0]) + " ", end='')
        print()

def main3():
  sol = Solution3()
  print("Total knapsack profit: " +
        str(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
  print("Total knapsack profit: " +
        str(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main3()
    

# ----------------------------------------------------------------

# Can we further improve our bottom-up DP solution? Can you find an algorithm that has O(C) space complexity?

# We only need one previous row to find the optimal solution!

class Solution4:
  def solveKnapsack(self, profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
      return 0

    # we only need one previous row to find the optimal solution, overall we need '2' rows
    # the above solution is similar to the previous solution, the only difference is that
    # we use `i % 2` instead if `i` and `(i-1) % 2` instead if `i-1`
    dp = [[0 for x in range(capacity+1)] for y in range(2)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
      if weights[0] <= c:
        dp[0][c] = dp[1][c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
      for c in range(0, capacity+1):
        profit1, profit2 = 0, 0
        # include the item, if it is not more than the capacity
        if weights[i] <= c:
          profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]
        # exclude the item
        profit2 = dp[(i - 1) % 2][c]
        # take maximum
        dp[i % 2][c] = max(profit1, profit2)

    return dp[(n - 1) % 2][capacity]


def main4():
  sol = Solution4()
  print("Total knapsack profit: " +
        str(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
  print("Total knapsack profit: " +
        str(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main4()

# The solution above is similar to the previous solution; the only difference is that we use i%2 instead of i and (i-1)%2 instead of i-1. This solution has a space complexity of O(2*C) = O(C), where ‘C’ is the knapsack’s maximum capacity.


# ------------------------------------------------------------------

# This space optimization solution can also be implemented using a single array. It is a bit tricky, but the intuition is to use the same array for the previous and the next iteration!

# If you see closely, we need two values from the previous iteration: dp[c] and dp[c-weight[i]]

# Since our inner loop is iterating over c:0-->capacity, let’s see how this might affect our two required values:

# When we access dp[c], it has not been overridden yet for the current iteration, so it should be fine.
# dp[c-weight[i]] might be overridden if “weight[i] > 0”. Therefore we can’t use this value for the current iteration.
# To solve the second case, we can change our inner loop to process in the reverse direction: c:capacity-->0. This will ensure that whenever we change a value in dp[], we will not need it again in the current iteration.

class Solution5:
  def solveKnapsack(self, profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
      return 0

    dp = [0 for x in range(capacity+1)]

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(0, capacity+1):
      if weights[0] <= c:
        dp[c] = profits[0]

    # process all sub-arrays for all the capacities
    for i in range(1, n):
      for c in range(capacity, -1, -1):
        profit1, profit2 = 0, 0
        # include the item, if it is not more than the capacity
        if weights[i] <= c:
          profit1 = profits[i] + dp[c - weights[i]]
        # exclude the item
        profit2 = dp[c]
        # take maximum
        dp[c] = max(profit1, profit2)

    return dp[capacity]


def main5():
  sol = Solution5()
  print("Total knapsack profit: " +
        str(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 7)))
  print("Total knapsack profit: " +
        str(sol.solveKnapsack([1, 6, 10, 16], [1, 2, 3, 5], 6)))


main5()
