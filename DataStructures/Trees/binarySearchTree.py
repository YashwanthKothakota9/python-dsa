class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def inOrderHelper(self, node):
        if node is not None:
            self.inOrderHelper(node.left)
            print(node.data,end=" ")
            self.inOrderHelper(node.right)

    def preOrderHelper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preOrderHelper(node.left)
            self.preOrderHelper(node.right)

    def postOrderHelper(self, node):
        if node is not None:
            self.postOrderHelper(node.left)
            self.postOrderHelper(node.right)
            print(node.data, end=" ")

    def findMin(self, node):
        if node.left is None:
            return node
        return self.findMin(node.left)

    def deleteNode(self, root, value):
        if root is None:
            return root
        if value < root.data:
            root.left = self.deleteNode(root.left,value)
        elif value > root.data:
            root.right = self.deleteNode(root.right,value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.findMin(root.right)
            root.data = temp.data
            root.right = self.deleteNode(root.right,temp.data)
        return root

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            parent = None

            while current is not None:
                parent = current
                if value < current.data:
                    current = current.left
                else:
                    current = current.right
            
            if value < parent.data: # type: ignore
                parent.left = new_node # type: ignore
            else:
                parent.right = new_node # type: ignore

    def deleteMethod(self, value):
        self.root = self.deleteNode(self.root,value)

    def search(self, value):
        current = self.root
        while current is not None:
            if current.data == value:
                return True
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def inOrder(self):
        self.inOrderHelper(self.root)
        print()

    def preOrder(self):
        self.preOrderHelper(self.root)
        print()

    def postOrder(self):
        self.postOrderHelper(self.root)
        print()


if __name__ == "__main__":
    obj = BST()
    obj.insert(5)
    obj.insert(3)
    obj.insert(7)
    obj.insert(2)
    obj.insert(4)
    obj.insert(6)
    obj.insert(8)
    
    obj.inOrder()
    obj.preOrder()
    obj.postOrder()

    obj.deleteMethod(2)

    obj.inOrder()
