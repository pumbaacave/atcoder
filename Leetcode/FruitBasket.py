from collections import Counter, deque
class Window():
    def __init__(self):
        self.elems = deque()
        self.counter = Counter()

    def __len__(self):
        return len(self.elems)

    def add(self, val):
        self.counter[val] += 1
        self.elems.append(val)

    def get_cardinality(self):
        return len(self.counter)

    def dropleft(self):
        if not self.elems:
            return
        head = self.elems.popleft()
        if self.counter[head] == 1:
            del self.counter[head]
        else:
            self.counter[head] -= 1

class Solution:
    def totalFruit(self, tree: 'List[int]') -> 'int':
        w = Window()
        tree = deque(tree)
        total_fruit = 0
        while tree:
            head = tree.popleft()
            w.add(head)
            if w.get_cardinality() <= 2:
                total_fruit = max(total_fruit, len(w))
            else:
                while w.get_cardinality() > 2:
                    w.dropleft()

        return total_fruit

def test_total_fruit_1():
    s = Solution()
    tree = [3,3,3,1,2,1,1,2,3,3,4]
    assert s.totalFruit(tree) == 5

def test_total_fruit_2():
    s = Solution()
    tree =[1,2,3,2,2]
    assert s.totalFruit(tree) == 4

def test_total_fruit_empty():
    s = Solution()
    tree = []
    assert s.totalFruit(tree) == 0

def test_window():
    w = Window()
    w.add(1)
    w.add(1)
    w.add(2)
    w.add(3)
    assert w.get_cardinality() == 3, "Wrong Cardinality"
    assert len(w) == 4, "Wrong Window length"
    w.dropleft()
    assert w.get_cardinality() == 3, "Wrong Cardinality"
    assert len(w) == 3, "Wrong Window length"
    w.dropleft()
    assert w.get_cardinality() == 2, "Wrong Cardinality"
    assert len(w) == 2, "Wrong Window length"
    w.dropleft()
    w.dropleft()
    w.dropleft()
    w.dropleft()
    assert w.get_cardinality() == 0, "Wrong Cardinality"
    assert len(w) == 0, "Wrong Window length"
