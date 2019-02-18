from collections import deque
class Node():
    """
    data node of a trie
    """
    def __init__(self, val):
        self.children = {}
        self.term = False
        self.val = val

class Tri():
    """
    trie for lowercase words
    #TODO with 26 character only
    use ord() to create key
    use fixed length list to hold children
    """
    def __init__(self):
        # dummy root node
        self.root = Node(None)

    def put(self, word):
        cur = self.root
        word = deque(word)
        while word:
            head = word.popleft()
            if head in cur.children:
                cur = cur.children[head]
            else:
                cur.children[head] = Node(head)
                cur = cur.children[head]

        cur.term = True

    def __contains__(self, word):
        word = deque(word)
        cur = self.root
        while word:
            head = word.popleft()
            if head in cur.children:
                cur = cur.children[head]
            else:
                return False
        return cur.term

def test_tri():


