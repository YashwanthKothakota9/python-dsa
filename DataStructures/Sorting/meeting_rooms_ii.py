# Given a list of time intervals during which meetings are scheduled, determine the minimum number of meeting rooms that are required to ensure that none of the meetings overlap in time.

# Examples
# Example 1:

# Input: [[10, 15], [20, 25], [30, 35]]
# Expected Output: 1
# Justification: There are no overlapping intervals in the given list. So, only 1 meeting room is enough for all the meetings.
# Example 2:

# Input: [[10, 20], [15, 25], [24, 30]]
# Expected Output: 2
# Justification: The first and second intervals overlap, and the second and third intervals overlap as well. So, we need 2 rooms.
# Example 3:

# Input: [[10, 20], [20, 30]]
# Expected Output: 1
# Justification: The end time of the first meeting is the same as the start time of the second meeting. So, one meeting can be scheduled right after the other in the same room.

# To determine the minimum number of rooms required to host the meetings without any time overlap, our approach first involves sorting all meeting intervals based on their start times. This sorting allows us to sequentially evaluate meetings in the order they start. We then utilize a priority queue (min-heap) to keep track of end times of the meetings currently taking place. This queue helps in efficiently determining the earliest ending meeting. By sequentially examining each meeting and comparing its start time to the earliest ending time from the heap, we can decide if a new room is needed or if an existing room can be reused.

import heapq
from typing import List

class Solution:
    def minMeetRooms(self, intervals:List[List[int]]) -> int:
        if not intervals:
            return 0
        
        free_rooms = []
        
        intervals.sort(key = lambda x:x[0])
        
        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms,intervals[0][1])
        
        # For all the remaining meeting rooms
        for i in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            # If a new room is to be assigned, then also we add to the heap.
            heapq.heappush(free_rooms, i[1])
        
        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

sol = Solution()
print(sol.minMeetRooms([[10, 15], [20, 25], [30, 35]])) # 1
print(sol.minMeetRooms([[10, 20], [15, 25], [24, 30]])) # 2
print(sol.minMeetRooms([[10, 20], [20, 30]])) # 1

        
        