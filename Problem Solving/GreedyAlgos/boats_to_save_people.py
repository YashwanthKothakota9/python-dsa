class Solution:
    def numBoats(self, people, limit):
        people.sort()
        i = 0
        j = len(people)-1
        boats = 0
        
        while i < j:
            # If the lightest and heaviest person can share a boat
            if people[i] + people[j] <= limit:
                i+=1# Move to the next lightest person
            j-=1 # Move to the next heaviest person
            boats += 1 # Increment boat count

            # When last person is left.
            if i==j:
                boats += 1
        return boats

solution = Solution()
people = [10, 55, 70, 20, 90, 85]
limit = 100

result = solution.numBoats(people, limit)
print("Minimum number of boats required:", result)
# Expected output: "Minimum number of boats required: 4"


# In the above problem, the greedy approach is applied through the strategy of pairing the lightest and heaviest individuals to optimize boat usage. After sorting the people by weight, the algorithm iteratively pairs the lightest person (at the start of the array) with the heaviest (at the end), maximizing the use of each boat's capacity. This method ensures that each boat carries as much weight as possible without exceeding the limit, effectively reducing the total number of boats needed.

# The essence of the greedy method here is making the most efficient pairing choice at each step, aiming for an overall optimal solution - the minimum number of boats to transport everyone.


