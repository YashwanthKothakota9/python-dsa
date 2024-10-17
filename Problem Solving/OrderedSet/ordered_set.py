class OrderedSet:
    def __init__(self):
        self.set = []

    def add(self, element):
        if element not in self.set:
            self.set.append(element)
            self.set.sort(reverse=True)

    def find_by_order(self, k):
        if k < 0 or k >= len(self.set):
            return None
        return self.set[k]

    def order_of_key(self, element):
        return sum(1 for x in self.set if x > element)


orderedSet = OrderedSet()
orderedSet.add(5)
orderedSet.add(1)
orderedSet.add(2)
print(orderedSet.set)
print(orderedSet.find_by_order(1))  # Find 2nd element in descending order
# Elements greater than 3 in descending order
print(orderedSet.order_of_key(3))


# Time and Space Complexity Analysis
# Time complexity: The time complexity for common operations like addition, removal, and searching in a TreeSet is O(logn), where n is the number of elements in the set. This is because TreeSet is typically implemented using a tree structure.
# Space complexity: The space complexity is O(n), as it needs to store each unique element.
# Let's jump onto our first problem and apply the Ordered set pattern.
