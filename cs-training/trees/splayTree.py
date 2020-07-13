
class TreeNode(object):
    def __init__(self, value: any=None):
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
        self.value: any = value

class SplayTree(object):
    def __init__(self):
        self._root: TreeNode = None
        self._size: int = 0

    def print_value(self) -> None:
        print(self._in_order(self._root))

    def root(self) -> TreeNode:
        return self._root

    def size(self) -> int:
        return self._size

    def insert(self, value: any) -> None:
        if not self._root: 
            self._size += 1
            self._root = TreeNode(value=value)
        else:
            z = self._root
            while z:
                if z.value < value:
                    if not z.right:
                        self._size += 1
                        z.right = TreeNode(value=value)
                        z.right.parent = z
                    z = z.right
                elif z.value > value:
                    if not z.left:
                        self._size += 1
                        z.left = TreeNode(value=value)
                        z.left.parent = z
                    z = z.left
                else:
                    break
            self._splay(z)

    def find(self, value: any) -> TreeNode:
        """
        此处的find实现没有对找到的节点伸展到根部
        因此查找的时间复杂度是O(n) （对应最坏情况，退化为链表）
        """
        z = self._root
        while z:
            if z.value < value: z = z.right
            elif z.value > value: z = z.left
            else: return z
        return None

    def delete(self, value: any) -> None:
        z = self.find(value)
        if not z: return

        self._splay(z)

        if not z.left: self._replace(z, z.right)
        elif not z.right: self._replace(z, z.left)
        else:
            """
            z右子树的最小值替换z，作为根
            """
            y = self._subtree_min(z.right)
            if y.parent is not z:
                self._replace(y, y.right)
                y.right = z.right
                z.right.parent = y
            self._replace(z, y)
            y.left = z.left
            y.left.parent = y

        self._size -= 1

    def min(self) -> any:
        return self._subtree_min(self._root)

    def max(self) -> any:
        return self._subtree_max(self._root)

    def _left_rotate(self, x: TreeNode) -> None:
        """
        P       P'
        
            X
          /   \
        Xl      Y
              /   \
            Yl      Yr(new)

        -------------------

            P       P'
            
                Y
              /   \
            X      Yr(new)
          /   \       
        Xl      Yl      
        """
        y = x.right
        if y:
            if y.left: y.left.parent = x
            x.right = y.left
            y.parent = x.parent
        
        if not x.parent: self._root = y
        elif x.parent.left is x: x.parent.left = y
        else: x.parent.right = y
        
        if y: y.left = x

        x.parent = y


    def _right_rotate(self, x: TreeNode) -> None:
        """
                P       P'
                
                    X
                  /   \
                Y      Xr
              /   \
          Yl(new)  Yr

        -------------------

            P       P'
            
                Y
              /   \
          Yl(new)  X    
                 /   \       
                Yr    Xr      
        """
        y = x.left
        if y:
            if y.right: y.right.parent = x
            x.left = y.right
            y.parent = x.parent
            y.right = x

        if not x.parent: self._root = y
        elif x.parent.left is x: x.parent.left = y
        else: x.parent.right = y

        x.parent = y

    def _splay(self, x: TreeNode) -> None:
        while x.parent:
            if x.parent.left is x: self._right_rotate(x.parent)
            else: self._left_rotate(x.parent)

    def _replace(self, u: TreeNode, v: TreeNode) -> None:
        """
        子树整体替换
        """
        if not u.parent: self._root = v
        elif u.parent.left is u: u.parent.left = v
        else: u.parent.right = v
        if v: v.parent = u.parent

    def _subtree_min(self, u: TreeNode) -> TreeNode:
        while u.left:
            u = u.left
        return u

    def _subtree_max(self, u: TreeNode) -> TreeNode:
        while u.right:
            u = u.right
        return u

    def _in_order(self, z: TreeNode) -> list:
        res = []
        if z:
            res.extend(self._in_order(z.left))
            res.append(z.value)
            res.extend(self._in_order(z.right))
        return res

if __name__ == '__main__':
    spl_tree = SplayTree()
    v = [101,122,1050,112,159,149,200,1,5,3,140,128,8,9,6,2,4,7]
    for vv in v:
        spl_tree.insert(vv)
    print('insert end')
    spl_tree.print_value()
    assert spl_tree.root().value == 7

    node = spl_tree.find(4)
    assert node.value == 4

    spl_tree.delete(4)
    spl_tree.print_value()
    print(spl_tree.root().value)

    spl_tree.insert(10)
    assert spl_tree.root().value == 10
    spl_tree.print_value()

    spl_tree.delete(12)
    assert spl_tree.root().value == 10
    spl_tree.print_value()

    spl_tree.insert(2)
    assert spl_tree.root().value == 2
    spl_tree.print_value()