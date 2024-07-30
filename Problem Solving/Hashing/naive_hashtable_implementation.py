class Record:
    def __init__(self, key=-1, title="", placement_info=""):
        self.Key = key
        self.Title = title
        self.PlacementInfo = placement_info

class HashTable:
    def __init__(self, size):
        # Pointer to store address of dynamically allocated array
        self.HT_array = [Record() for _ in range(size)]
        # To store maximum number of elements a Hash table can store
        self.max_length = size
        # To keep track of total records present in the hash table
        self.length = 0

    def __del__(self):
        # Cleanup the dynamically allocated array
        del self.HT_array

    # The Hash function
    def H(self, key):
        return key % self.max_length

    # Defining naive insertion
    def Insert(self, item):
        if self.length == self.max_length:
            print("Hash table is full. Cannot insert the key-value pair.")
            return False

        index = self.H(item.Key)
        self.HT_array[index] = item
        self.length += 1
        return True

    # Defining naive search
    def Search(self, key, returnedItem):
        index = self.H(key)
        if self.HT_array[index].Key == -1:
            # Record not found
            return False
        returnedItem.Key = self.HT_array[index].Key
        returnedItem.Title = self.HT_array[index].Title
        returnedItem.PlacementInfo = self.HT_array[index].PlacementInfo
        # Return true to indicate the record was found
        return True

    # Defining naive deletion
    def Delete(self, key):
        index = self.H(key)
        if self.HT_array[index].Key == key:
            # Mark the slot as empty
            self.HT_array[index].Key = -1
            self.length -= 1
            return True
        # The slot is already empty or there is a different item at the slot
        return False

# The driver code
if __name__ == "__main__":
    hashTable = HashTable(10)

    # Insert book information
    hashTable.Insert(Record(1001, "Introduction to Programming", "A2 Shelf"))
    hashTable.Insert(Record(1002, "Data Structures and Algorithms", "B1 Shelf"))
    hashTable.Insert(Record(1003, "Database Management Systems", "C3 Shelf"))

    # Retrieve book information
    book = Record()
    if hashTable.Search(1001, book):
        print("Book Information for Key", book.Key, ":")
        print("Title:", book.Title)
        print("Placement Info:", book.PlacementInfo)
    else:
        print("No book information found for Key 1001")

    # Delete a book information
    hashTable.Delete(1001)

    # Retrieve the book status after deletion
    if hashTable.Search(1001, book):
        print("Book Information for Key", book.Key, ":")
        print("Title:", book.Title)
        print("Placement Info:", book.PlacementInfo)
    else:
        print("No book information found for Key 1001")