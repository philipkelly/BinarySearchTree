class BinaryTree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
def closestValue(tree,target):
    return closestValueHelper(tree,target,tree.value)
def closestValueHelper(tree,target,closest):
    while tree is not None:
        if tree == target:
            return tree.value
        if abs(target-closest)>abs(target-tree.value):
            tree.value=closest
        if target<tree.value:
            tree=tree.left
        if target>tree.value:
            tree=tree.right
        else:
            break
    print(closest)
