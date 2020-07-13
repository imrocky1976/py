class Node:
    def __init__(self, value=None):
        self.left: Node = None
        self.right: Node = None
        self.value : any = value

def insert(bst: Node, value: any) -> Node:
    if bst is None:
        bst = Node(value)
        return bst
    p = bst
    while bst is not None:
        if value < bst.value:
            if bst.left is None:
                bst.left = Node(value)
                break
            else:
                bst = bst.left
        elif value > bst.value:
            if bst.right is None:
                bst.right = Node(value)
                break
            else:
                bst = bst.right
    return p

def delete(bst: Node, value: any) -> Node:
    if bst is None:
        return bst
    if value < bst.value:
        bst.left = delete(bst.left, value)
    elif value > bst.value:
        bst.right = delete(bst.right, value)
    else:
        if bst.left is None and bst.right is None:
            bst = None
        elif bst.left is None:
            bst = bst.right
        elif bst.right is None:
            bst = bst.left
        else:
            right_min = minValue(bst.right)
            bst.value = right_min
            bst.right = delete(bst.right, right_min)

    return bst

def minValue(bst: Node) -> any:
    min_value = bst.value
    while bst.left:
        min_value = bst.left.value
    return min_value 

def find(bst: Node, value: any) -> bool:
    if bst is None: return False
    if value < bst.value: return find(bst.left, value)
    if value > bst.value: return find(bst.right, value)
    return True

def inOrderTraverse(bst: Node) -> list:
    res = []
    if bst is not None:
        res.extend(inOrderTraverse(bst.left))
        res.append(bst.value)
        res.extend(inOrderTraverse(bst.right))

    return res


if __name__ == '__main__':
    values = [1,8,4,2,6,9,10]
    bst = None
    for value in values:
        bst = insert(bst, value)
    inOrder = inOrderTraverse(bst)
    print(inOrder)
    bst = delete(bst, 8)
    inOrder = inOrderTraverse(bst)
    print(inOrder)
    print(find(bst, 9))
    print(find(bst, 12))