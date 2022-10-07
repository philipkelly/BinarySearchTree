def minHeight(array):
    return findMiddle(array,None,0,len(array)-1)

#creating the recursive func
def findMiddle(array,bst,startIdx,endIdx):
    # base case:when we run out of values in a particular subtree
    # when the ending index is smaller than the starting index
    # if the endidx=startidx it means that we have one value left in the array to add
    if endIdx<startIdx:
        return
    midIdx=(startIdx+endIdx)//2 # going round it down
    valuetoadd=array[midIdx]

    # since we gave bst as none we have to handle the case
    if bst is None:
        bst=BST(valuetoadd)  # this is to add the root node if there is no BST
    else:
        bst.insert(valuetoadd)

    # this part is the recursive part for the left and right sub arrays

    # this is for the left sub array
    findMiddle(array,bst,startIdx,midIdx-1)

    # this is for the right sub array
    findMiddle(array,bst,midIdx+1,endIdx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
