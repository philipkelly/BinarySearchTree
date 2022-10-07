def inOrderTraversal(tree,array):
    if tree is not None:  #to make sure our tree is not a leaf node or empty
        inOrderTraversal(tree.left,array)
        # inOrderTraversal(tree.left.left,array)
        # this keeps going until it cant go left anymore
        array.append(tree.value)
        inOrderTraversal(tree.right,array)
    return array


def preOrderTraveral(tree,array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraveral(tree.left,array)
        preOrderTraveral(tree.right,array)
    return array

def postOrderTraversal(tree,array):
    if tree is not None:
        postOrderTraversal(tree.left,array)
        postOrderTraversal(tree.right,array)
        array.append(tree.value)
    return array

