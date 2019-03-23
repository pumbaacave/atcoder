from collections import deque
import random
import pdb


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST():
    def __init__(self, nums):
        self.create_bst(nums)

    def __contains__(self, val):
        pass

    def __getitem__(self, val):
        pass

    def __repr__(self):
        root = self.root
        queue = deque([root, "*"])
        while queue:
            cur = queue.popleft()
            if cur == "*":
                print("*" * 20)
                if len(queue) > 0:
                    queue.append(cur)
            elif not cur:
                print(cur)
            else:
                print(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)



    def create_bst(self, nums):
        if not nums:
            self.root = None
        elif len(nums) == 1:
            self.root = Node(nums[0])
        else:
            l, r = 0, len(nums) -1
            mid = l + (r - l)//2
            self.root = Node(nums[mid])
            rest =  nums[mid-1:0:-1] + nums[mid+1:]
            random.shuffle(rest)
            for i in rest:
                self.insert(nums[i])

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        cur = self.root
        while cur:
            if val < cur.val:
                if not cur.left:
                    cur.left = Node(val)
                    break
                else:
                    cur = cur.left
            elif val > cur.val:
                if not cur.right:
                    cur.right= Node(val)
                    break
                else:
                    cur = cur.right


def test_bst():
    nums = list(range(10))
    bst = BST(nums)
    pdb.set_trace()
    print(bst)
