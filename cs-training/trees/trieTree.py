
class TrieNode:
    def __init__(self):
        self.count = 0
        self.next = [None]*26

def insert(trie, string):
    curNode = trie
    for s in string:
        i = ord(s) - ord('a')
        if curNode.next[i] is None:
            curNode.next[i] = TrieNode()
        #curNode.next[i].count += 1
        curNode = curNode.next[i]
    curNode.count += 1

def search(trie, string):
    curNode = trie
    for s in string:
        i = ord(s) - ord('a')
        if curNode.next[i] is None:# or curNode.next[i].count == 0:
            return 0
        curNode = curNode.next[i]
    return curNode.count

if '__main__' == __name__:
    trie = TrieNode()
    words = ['you', 'are', 'a', 'dull', 'boy', 'dull']
    for word in words:
        insert(trie, word)
    
    print(search(trie, 'hehe'))

