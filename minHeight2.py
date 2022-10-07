#  this solution is more optimal time wise as we are not using he .insert function
def minheight(array):
    return findmiddle(array,0,len(array)-1)
def findmiddle(array,startidx,endidx):
    if endidx<startidx:
        return None
    midIdx=(startidx+endidx)//2
    bst=BST(array[midIdx])
    bst.left=findmiddle(array,0,midIdx-1)
    bst.right=findmiddle(array,midIdx+1,endidx)
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
