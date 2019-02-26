class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        num_vec = len(graph)
        # init node i to group i
        parent = [i for i in range(num_vec)]
        self.parent = parent
        for i, v_list in enumerate(graph):
            if not v_list:
                continue
            root_of_child = self.find_root(v_list[0])
            for v in v_list:
                # two connected vertex are in the same group
                # the graph is not bipartie
                if self.find_root(i) == self.find_root(v):
                    return False
                self.union(root_of_child, v)

        return True

    def find_root(self, vertex):
        parent = self.parent[vertex]
        root = vertex if parent == vertex else self.find_root(parent)
        return root
    
    def union(self, root, vertex):
        self.parent[vertex] = root
                
            

        