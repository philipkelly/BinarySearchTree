

def validateBST(tree):
    return validateBSThelper(tree,float("-inf"),float("inf"))
    #  setting the helpers max and min to infinity and -infinity
def validateBSThelper(tree,minvalue,maxvalue):
    # we need to check if we are at a leaf node
    if tree is None:
        return True
    # now we are gonna check if the node we are at is between the min and max value
    if tree.value<minvalue or tree.value>=maxvalue:
        return False
    # the node of the tree has to be more than or equal to the min.value and less than the max value

    # now we want to check if the left subtree is valid
    leftIsValid=validateBSThelper(tree.left,minvalue,tree.value)
    # think of it as left is valid = check ( current value= left of the root node, minvalue=-inf,current value=root)
    # the node immediately to the left of the node has to have a max value of our tree value
    return leftIsValid and validateBSThelper(tree.right,tree.value,maxvalue)
