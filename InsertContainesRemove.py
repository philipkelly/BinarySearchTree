class BST:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

    def insert(self, value):
        currentnode = self
        while True:
            # value is the value we are trying to insert
            if value < currentnode.value:  # if the value we are trying to insert is less than the current nodes value we know we want to go left
                if currentnode.left is None:  # if the current node has no left node
                    currentnode.left = BST(value)  # we insert the value into the left postition
                    break
                else:
                    # if there is still values on the left sub tree we update the current node to move down to the left
                    currentnode = currentnode.left  # we assign the current node to be the current node. left
            else:
                if currentnode.right is None:
                    currentnode.right = BST(value)
                    break
                else:
                    currentnode = currentnode.right

        return self

    def contains(self, value):
        currentnode = self
        while currentnode is not None:
            if value < currentnode.value:
                currentnode = currentnode.left
            elif value > currentnode.value:
                currentnode = currentnode.right
            else:
                return True
        return False