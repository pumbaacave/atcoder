class Solution:
    # return the flipped node val list
    def flipMatchVoyage(self, root: 'TreeNode', voyage: 'List[int]') -> 'List[int]':
        if len(voyage) == 1 and voyage[0] == root.val:
            return []

        if voyage[0] != root.val:
            return [-1]

        flip = []
        l, r = root.left, root.right
        if l is None and r is None:
            return [-1]
        # invalid voyage for the tree
        if (l and l.val not in voyage) or (r and r.val not in voyage):
            return [-1]

        if r is None or l is None:
            node = l if not l else r
            idx = voyage.index(node.val)
            flip = self.flipMatchVoyage(node, voyage[idx:])
            return flip
        else:
            idx_l = voyage.index(l.val)
            idx_r = voyage.index(r.val)
            if idx_l > idx_r:
                flip.append(root.val)
                idx_l, idx_r = idx_r, idx_l

            flip += self.flipMatchVoyage(r, voyage[idx_r:])
            flip += self.flipMatchVoyage(l, voyage[idx_l:idx_r])

        if any(filter(lambda x: x<0, flip)):
            return [-1]
        else:
            return flip
