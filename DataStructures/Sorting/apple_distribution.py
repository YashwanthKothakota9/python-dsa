class Solution:
    def distributeApples(self, apples, capacity):
        capacity.sort()
        totalApples = sum(apples)
        
        i = len(capacity)-1
        while i >=0  and totalApples > 0:
            totalApples -= capacity[i]
            i-=1
            
        return len(capacity)-i-1

sol = Solution()

# Example 1
apples1 = [2, 3, 1]
capacity1 = [4, 2 ,5, 1]
print("output is", sol.distributeApples(apples1, capacity1))

# Example 2
apples2 = [4, 5, 6]
capacity2 = [5, 10]
print("output is", sol.distributeApples(apples2, capacity2))

# Example 3
apples3 = [1, 2, 5, 6]
capacity3 = [2, 3, 7, 4, 5, 2, 4]
print("output is", sol.distributeApples(apples3, capacity3))
