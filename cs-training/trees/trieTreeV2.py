class Node:
    def __init__(self):
        self.children: dict[str, Node] = {} # dict[str, Node]
        self.value: any = None

def find(node: Node, key: str) -> any:
    for char in key:
        if char in node.children:
            node = node.children[char]
        else:
            return None
    return node.value

def insert(node: Node, key: str, value: any) -> None:
    for char in key:
        if char not in node.children:
            node.children[char] = Node()
        node = node.children[char]
    node.value = value

if __name__ == '__main__':
    trie = Node()
    words = ['you', 'are', 'a', 'dull', 'boy', 'dull']
    for word in words:
        insert(trie, word, word)
    
    print(find(trie, 'a'))