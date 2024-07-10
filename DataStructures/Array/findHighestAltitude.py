# A bike rider is going on a ride. The road contains n + 1 points at different altitudes. The rider starts from point 0 at an altitude of 0.

# Given an array of integers gain of length n, where gain[i] represents the net gain in altitude between points i and i + 1 for all (0 <= i < n), return the highest altitude of a point.

# Example 1
# Input: gain = [-5, 1, 5, 0, -7]
# Expected Output: 1
# Justification: The altitude changes are [-5, -4, 1, 1, -6], where 1 is the highest altitude reached.

class Solution:
    def largestAltitude(self, gain):
        current_altitude = 0  # To store the current altitude during iteration
        max_altitude = 0  # To store the maximum altitude encountered

        # Iterate through the gain list, updating the current and max altitudes
        for i in gain:
            current_altitude += i
            max_altitude = max(current_altitude, max_altitude)

        return max_altitude

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    print(solution.largestAltitude([-5, 1, 5, 0, -7]))  # Expected: 1

    # Example 2
    print(solution.largestAltitude([4, -3, 2, -1, -2]))  # Expected: 4
    
    # Example 3
    print(solution.largestAltitude([2, 2, -3, -1, 2, 1, -5]))  # Expected: 4
