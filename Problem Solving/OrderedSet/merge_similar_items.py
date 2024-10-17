# Given two 2D arrays of item-value pairs, named items1 and items2.

# item[i] = [valuei, weighti], where each valuei in these arrays is unique within its own array and is paired with a weighti.
# Combine these arrays such that if a value appears in both, its weights are summed up. The final merged array should be sorted based on the valuei.

# Examples
# Example 1:

# Input: items1 = [[1,2],[4,3]], items2 = [[2,1],[4,3],[3,4]]
# Expected Output: [[1,2],[2,1],[3,4],[4,6]]
# Justification: Item 1 has value 2 in items1 and doesn't exist in items2, item 2 has value 1 in items2, item 4 is summed up.
# Example 2:

# Input: items1 = [[5,5]], items2 = [[5,10]]
# Expected Output: [[5,15]]
# Justification: Item 5 exists in both arrays, so their values are summed.
# Example 3:

# Input: items1 = [[1,1],[2,2]], items2 = [[3,3]]
# Expected Output: [[1,1],[2,2],[3,3]]
# Justification: All items are unique across items1 and items2, so they remain unchanged.

# To solve this problem, the approach involves creating a map (or dictionary) to efficiently track and combine the quantities of items. Start by iterating through each list. For each pair in these lists, check if the item (the first element of the pair) already exists in the map. If it does, update its quantity by adding the new quantity. If it doesn't exist, add the item and its quantity to the map. Once both lists are processed, you will have a map with each item and its total quantity. Finally, convert this map into a list of pairs, sorted by the item numbers. This list represents the merged and sorted items with their cumulative quantities.

# Step-by-step algorithm
# Merging Lists: Start by merging both lists into a single list. This step doesn't combine the values of similar items yet; it just creates a single list containing all item-value pairs.

# Using an Ordered Set: Create an ordered set (like TreeSet or TreeMap in Java or std::set in C++) to store the final item-value pairs. The key of the set will be the item identifier, and the value will be the sum of values for that item.

# Populating the Set: Iterate through the merged list. For each item-value pair, check if the item is already in the set. If it is, update the value by adding the new value to the existing one. If it's not, insert the new item-value pair into the set.

# Creating the Result List: Finally, iterate through the ordered set and construct the result list from the elements of the set.

# This approach ensures that each item is processed only once, making it efficient. The use of an ordered set guarantees that the final list is sorted by the item identifiers, as required.

# Algorithm Walkthrough for Example 1
# Let's walk through the algorithm using Example 1, where items1 = [[1,2],[4,3]] and items2 = [[2,1],[4,3],[3,4]].

# Initialization: Create an empty map (TreeMap in Java) to store the sum of values for each item. This map will help in merging and summing the item values.

# Processing items1:

# Process item [1,2]: Since item 1 is not in the map, add it with the value 2.
# Process item [4,3]: Since item 4 is not in the map, add it with the value 3.
# After processing items1, the map looks like {1=2, 4=3}.
# Processing items2:

# Process item [2,1]: Since item 2 is not in the map, add it with the value 1.
# Process item [4,3]: Item 4 already exists in the map with value 3, so update it to 3 + 3 = 6.
# Process item [3,4]: Since item 3 is not in the map, add it with the value 4.
# After processing items2, the map looks like {1=2, 2=1, 3=4, 4=6}.
# Creating Sorted Result:

# Convert the map entries into a list. The TreeMap ensures that entries are sorted based on the item identifiers.
# The resulting list from the map entries is [[1,2], [2,1], [3,4], [4,6]].
# Final Output:

# Return the sorted list [[1,2], [2,1], [3,4], [4,6]].


from collections import defaultdict


class Solution:
    def mergeSimilarItems(self, items1, items2):
        # Using defaultdict to automatically handle non-existing keys
        merged_items = defaultdict(int)

        # Process items from the first list
        for item, value in items1:
            merged_items[item] += value

        # Process items from the second list
        for item, value in items2:
            merged_items[item] += value

        # Sort and return the result based on item ID
        return sorted([[item, value] for item, value in merged_items.items()])


if __name__ == "__main__":
    solution = Solution()
    # Example inputs
    print(solution.mergeSimilarItems(
        [[1, 2], [4, 3]], [[2, 1], [4, 3], [3, 4]]))
    print(solution.mergeSimilarItems([[5, 5]], [[5, 10]]))
    print(solution.mergeSimilarItems([[1, 1], [2, 2]], [[3, 3]]))


# Time and Space Complexity Analysis
# Time Complexity: O(N log N), where N is the total number of item-value pairs. This accounts for the merging and sorting operations.
# Space Complexity: O(N), for storing the merged items and the result array.
