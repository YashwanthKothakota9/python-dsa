# Given two sorted arrays, nums1 and nums2 of different sizes in the ascending order, return the median of two sorted arrays after merging them.

# The median is the middle value in an ordered set, or the average of the two middle values if the set has an even number of elements.

# Examples
# Example 1:

# Input: [1, 3, 5] and [2, 4, 6]
# Expected Output: 3.5
# Justification: When merged, the array becomes [1, 2, 3, 4, 5, 6]. The median is the average of the middle two values, (3 + 4) / 2 = 3.5.
# Example 2:

# Input: [1, 1, 1] and [2, 2, 2]
# Expected Output: 1.5
# Justification: The merged array is [1, 1, 1, 2, 2, 2]. The median is (1 + 2) / 2 = 1.5.
# Example 3:

# Input: [2, 3, 5, 8] and [1, 4, 6, 7, 9]
# Expected Output: 5
# Justification: The merged array would be [10, 15, 20, 25, 30, 35, 40, 45]. The median is the average of the middle two values, 25 and 30, which is (25 + 30) / 2 = 27.5.

# To find the median of two sorted arrays, we can use the merge step of the merge sort algorithm and the two-pinter approach. This approach involves merging the elements of both arrays into a single sorted sequence. However, unlike traditional merge sort, we don't need to merge the entire arrays. Instead, we only merge until we reach the median position.

# The median position is determined by the combined size of the arrays, varying if the total number of elements is odd or even. The process involves comparing the elements at the pointer positions and advancing the pointer at the smaller element, thus mimicking a partial merge.

# This step continues until the pointers reach the median position. The median is then calculated based on the last elements encountered by the pointers: directly for an odd total and as an average of the last two elements for an even total.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return Solution.findMedianSortedArrays(self, nums2, nums1)
        
        totalLength = len(nums1) + len(nums2)
        isEven = totalLength % 2 == 0
        
        pointer1, pointer2 = 0, 0
        current = last = 0
        
        for count in range(totalLength // 2 + 1):
            last = current
            
            if pointer1 == len(nums1):
                current = nums2[pointer2]
                pointer2 += 1
            elif pointer2 == len(nums2) or nums1[pointer1] < nums2[pointer2]:
                current = nums1[pointer1]
                pointer1 += 1
            else:
                current = nums2[pointer2]
                pointer2 += 1
        median = (current + last) / 2.0 if isEven else current
        return round(float(median), 1)
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print("Median of Example 1:", sol.findMedianSortedArrays([1, 3, 5], [2, 4, 6]))

    # Example 2
    print("Median of Example 2:", sol.findMedianSortedArrays([1, 1, 1], [2, 2, 2]))

    # Example 3
    print("Median of Example 3:", sol.findMedianSortedArrays([2, 3, 5, 8], [1, 4, 6, 7, 9]))
