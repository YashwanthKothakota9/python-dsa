# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

# Example 1:

# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can occur in any of the two rooms later.
# Example 2:

# Meetings: [[6,7], [2,4], [8,12]]
# Output: 1
# Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
# Example 3:

# Meetings: [[1,4], [2,3], [3,6]]
# Output:2
# Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to hold all the meetings.
# Example 4:

# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].


# Let’s take the above-mentioned example (4) and try to follow our Merge Intervals approach:

# Meetings: [[4,5], [2,3], [2,4], [3,5]]

# Step 1: Sorting these meetings on their start time will give us: [[2,3], [2,4], [3,5], [4,5]]

# Step 2: Merging overlapping meetings:

# [2,3] overlaps with [2,4], so after merging we’ll have => [[2,4], [3,5], [4,5]]
# [2,4] overlaps with [3,5], so after merging we’ll have => [[2,5], [4,5]]
# [2,5] overlaps [4,5], so after merging we’ll have => [2,5]
# Since all the given meetings have merged into one big meeting ([2,5]), does this mean that they all are overlapping and we need a minimum of four rooms to hold these meetings? You might have already guessed that the answer is NO! As we can clearly see, some meetings are mutually exclusive. For example, [2,3] and [3,5] do not overlap and can happen in one room. So, to correctly solve our problem, we need to keep track of the mutual exclusiveness of the overlapping meetings.

# We can conclude that we need to keep track of the ending time of all the meetings currently happening so that when we try to schedule a new meeting, we can see what meetings have already ended. We need to put this information in a data structure that can easily give us the smallest ending time. A Min Heap would fit our requirements best.


# Time Complexity
# The time complexity of the above algorithm is O(NlogN), where ‘N’ is the total number of meetings. This is due to the sorting that we did in the beginning. Also, while iterating the meetings we might need to poll/offer meeting to the priority queue. Each of these operations can take O(logN). Overall our algorithm will take O(NlogN).

# Space Complexity
# The space complexity of the above algorithm will be O(N) which is required for sorting. Also, in the worst case scenario, we’ll have to insert all the meetings into the Min Heap (when all meetings overlap) which will also take O(N) space. The overall space complexity of our algorithm is O(N).

# Similar Problems
# Problem 1: Given a list of intervals, find the point where the maximum number of intervals overlap.

# Problem 2: Given a list of intervals representing the arrival and departure times of trains to a train station, our goal is to find the minimum number of platforms required for the train station so that no train has to wait.

# Both of these problems can be solved using the approach discussed above.




import heapq

class Meeting:
    def __init__(self, start, end):
        self.start = start
        self.end = end

setattr(Meeting, "__lt__", lambda self, other: self.end < other.end)


class Solution:
    def findMinimumMeetingRooms(self, meetings):
        if not meetings:
            return 0

        meetings.sort(key = lambda x: x.start)
        
        minRooms = 0
        minHeap = []
        
        for meeting in meetings:
            # remove all meetings that have ended
            while minHeap and meeting.start > minHeap[0].end:
                heapq.heappop(minHeap)
            
            # add the current meeting into the minHeap
            heapq.heappush(minHeap, meeting)
            
            # all active meetings are in the minHeap, so we need rooms for all of them.
            minRooms = max(minRooms, len(minHeap))
        
        return minRooms
    

if __name__ == "__main__":
    sol = Solution()
    inputs = [
        [Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)],
        [Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)],
        [Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)],
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)]
    ]

    for input in inputs:
        result = sol.findMinimumMeetingRooms(input)
        print("Minimum meeting rooms required:", result)