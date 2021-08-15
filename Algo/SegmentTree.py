from operator import add

ROOT = 0

class SegmentTree():
    """
    https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
    """
    def __init__(self, nums):
        num_length = len(nums)
        tree = [0] * 4 * num_length

        self.nums = nums
        self.tree = tree
        if num_length != 0:
            self.build_seg_tree(0, 0, num_length - 1)

    def merge(self, A, B):
        return add(A, B)

    def build_seg_tree(self, tree_idx, lo, hi):
        if lo == hi:
            self.tree[tree_idx] = self.nums[lo]
            return None

        mid = ( lo + hi ) // 2
        self.build_seg_tree(2 * tree_idx + 1, lo, mid)
        self.build_seg_tree(2 * tree_idx + 2, mid + 1, hi)

        self.tree[tree_idx] = self.merge(self.tree[2 * tree_idx + 1], self.tree[2 * tree_idx + 2])

    def query(start_node_idx, end_node_idx):
        """
        query the whole tree
        @param start_node_idx is inclusive
        @param end_node_idx is inclusive
        """
        return query_seq_tree(ROOT, ROOT, len(self.num)- 1, start_node_idx, end_node_idx)


    def query_seg_tree(self, tree_idx, lo, hi, i, j):
        """
        tree_idx holds value of nums[lo:hi+1] :: lo...hi
        query is for nums[i:j]
        """
        # when nums == []
        if hi < lo:
            return 0
        if j < lo or hi < i:
            return 0
        if i <= lo and hi <= j:
            return self.tree[tree_idx]

        mid = ( lo + hi ) // 2
        if i > mid:
            return self.query_seg_tree(2 * tree_idx + 2, mid + 1, hi, i, j)
        elif j <= mid:
            return self.query_seg_tree(2 * tree_idx + 1, lo, mid, i, j)

        left_q = self.query_seg_tree(2 * tree_idx + 1, lo, mid, i, mid)
        right_q = self.query_seg_tree(2 * tree_idx + 2, mid + 1, hi, mid + 1, j)
        return self.merge(left_q, right_q)

    def update_seg_tree(self, tree_idx, lo, hi, nums_idx, val):
        if lo == hi:
            self.tree[tree_idx] = val
            self.nums[nums_idx] = val
            return
        mid = ( lo + hi ) // 2
        if nums_idx > mid:
            self.update_seg_tree(2 * tree_idx + 2, mid + 1, hi, nums_idx, val)
        elif nums_idx <= mid:
            self.update_seg_tree(2 * tree_idx + 1, lo, mid, nums_idx, val)

        self.tree[tree_idx] = self.merge(self.tree[2 * tree_idx + 1], self.tree[2 * tree_idx + 2])

    def __repr__(self):
        return "original nums array: "+str(self.nums) + '\n' +\
        "segment tree: "+ str(self.tree)

def test_empth():
    nums = []
    s = SegmentTree(nums)
    L = len(nums)
    q = s.query_seg_tree(0, 0, L - 1, 0, 5)
    assert q == 0

def test_query_update():
    nums = list(range(10))
    L = len(nums)
    s = SegmentTree(nums)
    # the #0 node holds value of nums 0..9, total 10 values
    q = s.query_seg_tree(0, 0, L - 1, 0, 5)
    print(s)
    assert q == 15
    s.update_seg_tree(0, 0, L - 1, 3, 100)

    q = s.query_seg_tree(0, 0, 9, 0, 5)
    print(s)
    assert q == 112

def test_query():
    nums = [-2, 0, 3, -5, 2, -1]
    s = SegmentTree(nums)
    print(s)
    L = len(nums)
    q = s.query_seg_tree(0, 0, L - 1, 0, 2)
    assert q == 1
    q = s.query_seg_tree(0, 0, L - 1, 2, 5)
    assert q == -1
    q = s.query_seg_tree(0, 0, L - 1, 0, 5)
    assert q == -3
