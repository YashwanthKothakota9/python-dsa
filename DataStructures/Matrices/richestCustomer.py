# You are given an m x n matrix accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank.

# Return the wealth that the richest customer has.

# Imagine every customer has multiple bank accounts, with each account holding a certain amount of money. The total wealth of a customer is calculated by summing all the money across all their multiple.

class Solution:
    def maximum_wealth(self,accounts):
        max_wealth = 0
        for customer in accounts:
            wealth = sum(customer)
            max_wealth = max(max_wealth, wealth)
        return max_wealth
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maximum_wealth([[5,2,3],[0,6,7]]))  # 13
    print(sol.maximum_wealth([[1,2],[3,4],[5,6]]))  # 11
    print(sol.maximum_wealth([[10,100],[200,20],[30,300]]))  # 330
