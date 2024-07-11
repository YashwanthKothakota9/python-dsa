class Record:
    def __init__(self, key, title, placement_info):
        self.Key = key
        self.Title = title
        self.PlacementInfo = placement_info

class HashTable:
    def __init__(self, size):
        self.buckets = [[] for _ in range(size)]
        self.max_length = size

    def H(self, key):
        return key % self.max_length

    def Insert(self, item):
        index = self.H(item.Key)

        # Check if the key already exists in the chain
        for record in self.buckets[index]:
            if record.Key == item.Key:
                return False  # Key already exists in the chain, cannot insert

        self.buckets[index].append(item)
        return True

    def Search(self, key, returnedItem):
        index = self.H(key)

        # Search for the key in the chain
        for record in self.buckets[index]:
            if record.Key == key:
                returnedItem.Key = record.Key
                returnedItem.Title = record.Title
                returnedItem.PlacementInfo = record.PlacementInfo
                return True  # Return True to indicate the record was found

        return False  # Record not found

    def Delete(self, key):
        index = self.H(key)

        # Search for the key in the chain and delete if found
        for i, record in enumerate(self.buckets[index]):
            if record.Key == key:
                del self.buckets[index][i]
                return True

        return False  # The key is not found in the chain

    def ShowTable(self):
        print("Index\tValue (Key, Title, PlacementInfo)")
        for i in range(self.max_length):
            print(i, end="\t")
            if not self.buckets[i]:
                print("[EMPTY BUCKET]")
            else:
                for j, record in enumerate(self.buckets[i]):
                    if j > 0:
                        print("-->", end=" ")
                    print("({0}, {1}, {2})".format(record.Key, record.Title, record.PlacementInfo), end=" ")
                print()

def main():
    tableSize = 11
    hashTable = HashTable(tableSize)

    # Insert initial book information
    hashTable.Insert(Record(1701, "Internet of Things", "G1 Shelf"))
    hashTable.Insert(Record(1712, "Statistical Analysis", "G1 Shelf"))
    hashTable.Insert(Record(1718, "Grid Computing", "H2 Shelf"))
    hashTable.Insert(Record(1735, "UML Modeling", "G1 Shelf"))
    hashTable.Insert(Record(1752, "Professional Practices", "G2 Shelf"))

    # Display the hash table after initial insertions
    print("\nHash Table after initial insertions:")
    hashTable.ShowTable()

    # Insert the following record
    hashTable.Insert(Record(1725, "Deep Learning with Python", "C3 Shelf"))

    # Display the hash table after the last insertion
    print("\nHash Table inserting Book Key 1725:")
    hashTable.ShowTable()

    # Delete two records
    hashTable.Delete(1701)
    hashTable.Delete(1718)

    # Display the hash table after deletions
    print("\nHash Table after deleting 1701 and 1718:")
    hashTable.ShowTable()

if __name__ == "__main__":
    main()