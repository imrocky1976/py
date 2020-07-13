# https://en.wikipedia.org/wiki/Red%E2%80%93black_tree

class Node:
    def __init__(self):
        self.color: str = 'r' # default color is red
        self.left: Node = None
        self.right: Node = None
        self.value: any = None

def insert(root: Node, value: any) -> Node:
    # 1. 新插入的节点记X。X设为红色标记，Node的默认构造已经满足

    # 2. 新节点X是根节点，标记为黑色
    if root is None:
        root = Node(value)
        root.color = 'b'
        return root
    
    # 按照bst树的方式将X插入rbTree
    p = root
    cur = None
    while p is not None:
        if value < p.value:
            if p.left is None:
                cur = p.left = Node(value)
                break
            else:
                p = p.left
        elif value > p.value:
            if p.right is None:
                cur = p.right = Node(value)
                break
            else:
                p = p.right

    fix_rbtree(root, cur) # 修正，使其满足rbTree
    return root

def fix_rbtree(root, cur):
    # 获取X的父和祖父节点
    p, pp = trace_back(root, cur)

    # 如果父是黑色，由于x是红色，则满足rbTree，这种情况无需考虑

    # 3. 如果X不是根，且X的父不是黑色
    while cur is not root and p.color == 'r':
        # 获取X的叔叔
        if pp.left is p:
            uncle = pp.right
        else:
            uncle = pp.left
        
        if uncle and uncle.color == 'r': # 3.1 如果X的叔叔是红色
            # 3.1.1 将父和叔叔标记为黑色
            p.color = 'b'
            uncle.color = 'b'
            # 3.1.2 祖父标记为红色
            pp.color = 'r'
            # 3.1.3 祖父设为新节点X
            cur = pp
            # 3.1.4 如果X是根节点，则标记为黑色，结束
            if cur is root:
                cur.color = 'b'
                break
            # 获取新X的父和祖父，重复步骤3
            p, pp = trace_back(root, cur)
        else: # 3.2 如果X的叔叔是黑色（None的时候也是黑色）
            # 分四种情况处理旋转


def trace_back(root: Node, cur: Node) - > (Node, Node):
    if root is None:
        return None, None
    now = root
    p = pp = None
    while now.value != cur.value:
        pp = p
        p = now
        if now.value < cur.value:
            now = now.right
        else:
            now = now.left
    return p, pp

def find(root: Node, value: any) -> bool:
    pass

def delete(root: Node, value: any) -> Node:
    pass