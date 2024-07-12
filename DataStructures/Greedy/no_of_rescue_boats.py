class Solution:
    def numOfRescueBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people)-1
        boats = 0
        while i<j:
            if people[i] + people[j] <= limit:
                i+=1
            j-=1
            boats += 1
            
            if i==j:
                boats += 1
        return boats

solution = Solution()
people = [10, 55, 70, 20, 90, 85]
limit = 100

result = solution.numOfRescueBoats(people, limit)
print("Minimum number of boats required:", result)
# Expected output: "Minimum number of boats required: 4"