def print_MinHeap(arr):
    print("Min Heap: ",arr)

def heapify(arr, size, index):
    smallestValue = index
    leftChild = 2 * index + 1
    rightChild = 2 * index + 2
    
    if leftChild < size and arr[leftChild] < arr[smallestValue]:
        smallestValue = leftChild
    
    if rightChild < size and arr[rightChild] < arr[smallestValue]:
        smallestValue = rightChild
    
    if smallestValue != index:
        arr[index], arr[smallestValue] = arr[smallestValue], arr[index]
        heapify(arr,size,smallestValue)

def insert_MinHeap(arr, value):
    arr.append(value)
    size = len(arr)
    
    for index in range((size//2)-1,-1,-1):
        heapify(arr,size,index)
        
min_heap = []
insert_MinHeap(min_heap, 5)
print_MinHeap(min_heap)

insert_MinHeap(min_heap, 2)
print_MinHeap(min_heap)

insert_MinHeap(min_heap, 8)
print_MinHeap(min_heap)