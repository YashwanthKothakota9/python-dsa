# Given a 2D array nums of size N x 2.

# nums[i] = [starti, endi], where starti is the starting time of the event and endi is the ending time of the event.
# For each nums[i], determine if a requested booking time conflicts with any existing bookings.

# Return a boolean array of size N, representing whether the booking can be done in the given time interval.

# Examples
# Example 1:

# Input: nums = [[10, 20], [15, 25], [20, 30]]
# Expected Output: [true, false, true]
# Justification: The first event is booked successfully. The second event overlaps with the first one and is rejected. The third event starts when the first event ends, so it's booked successfully.
# Example 2:

# Input: [[5, 10], [10, 15], [5, 15]]
# Expected Output: [true, true, false]
# Justification: The first and second events are booked without overlap. The third event overlaps with both the first and second, so it's rejected.
# Example 3:

# Input: [[8, 13],[13, 17], [17, 20]]
# Expected Output: [true, true, true]
# Justification: All events are booked without any overlap, as each event starts exactly when the previous one ends.
# Constraints:

# 0 <= start < end <= 109
# At most 1000 calls will be made to book.
# Solution
# To solve this problem, we manage event scheduling in a personal calendar using a TreeSet, a sorted data structure, to store events in order of their start times. The core of the solution involves processing an array of events, where each event is checked for potential overlaps with already scheduled events. This is done by comparing each new event with its closest neighbors in the TreeSet – the nearest events before and after it. If the new event doesn't overlap with these neighbors (i.e., it starts after the preceding event ends and ends before the subsequent event begins), it's added to the TreeSet. Otherwise, it's rejected. This approach efficiently handles multiple event bookings in one operation, ensuring that no two events overlap in the calendar.

# Initialization:

# Create a data structure (SortedSet in C#, TreeSet in Java, set in C++, and a list in Python and JavaScript) to store the booked intervals. This data structure will help maintain the intervals in a sorted order based on their start times.
# Booking Process:

# When a new booking request comes in (represented by a start and end time), we need to determine if it overlaps with any existing bookings.
# Check for two conditions:
# The new booking starts after or exactly when the previous booking ends.
# The new booking ends on or before the next booking starts.
# If both conditions are met, the booking does not overlap with existing bookings, and we can add it to our data structure.
# Insertion:

# If the booking is successful (i.e., no overlap), add the new interval to the data structure.
# Returning Results:

# The function should return a boolean value indicating whether the booking was successful (true) or not (false).
# Example Walkthrough
# Let's consider the example where we have the following booking requests: [[10, 20], [15, 25], [20, 30]].

# Booking [10, 20]:

# The booking list is empty, so this interval is added without any overlap. The list now contains [10, 20].
# Result: true
# Booking [15, 25]:

# We check this against the existing booking [10, 20]. The new booking starts before the existing one ends (15 < 20), so this is an overlap.
# Result: false
# Booking [20, 30]:

# We check this against the existing booking [10, 20]. The new booking starts exactly when the existing one ends (20 == 20), so there is no overlap.
# The booking [20, 30] is added to the list. The list now contains [10, 20] and [20, 30].
# Result: true
# So, the final results of these booking attempts are [true, false, true].


class Solution:
    bookings = []  # Static list to store bookings

    @staticmethod
    def book(nums):
        results = []  # List to store the results of booking attempts
        for start, end in nums:
            # Check for overlap with existing bookings
            for s, e in Solution.bookings:
                if s < end and start < e:
                    results.append(False)  # Overlap found, booking fails
                    break
            else:
                # No overlap, add booking
                Solution.bookings.append((start, end))
                results.append(True)  # Booking successful
        return results


if __name__ == "__main__":
    nums = [(10, 20), (15, 25), (20, 30)]
    print(Solution.book(nums))  # Print results of all bookings


# Complexity Analysis
# Time Complexity: The primary operations are searching and inserting in the ordered set. Both operations have an average time complexity of O(log n), where n is the number of events in the set.
# Space Complexity: The space complexity is O(n), as we need to store each event in the set.
