import bisect
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height = height
        l = 0
        r = 1
        # need sored tuple list
        # key: value = height: index
        # sorted by descending order
        length = len(height)
        scanned = []
        scanned.insert(0, (0, height[0]))
        self.add_to(scanned, (1, height[1]))
        max_water = min(height)
        if length == 2:
            return max_water
        # start from 2
        for i in range(2, length):
            if height[i] >= height[r]:
                scanned.append((i, height[i]))
                r = i
                max_water = self.cal_water_simple(l, r)
            else: # new container is larger
                new_l, new_max_water = self.cal_water_new(scanned, i)
                if new_max_water > max_water:
                    l = new_l
                    r = i
                    max_water = new_max_water
        return max_water

    @staticmethod
    def add_to(scanned, idx_height):
       for i in range(len(scanned)):
           if idx_height[1] <= scanned[i][1]:
               scanned.insert(i, idx_height)
               return i
       scanned.append(idx_height)
       return len(scanned)-1

    
    def cal_water_simple(self, l, r):
        return (r - l) * min(self.height[r], self.height[l])

    
    def cal_water_new(self, scanned, new_r):
        inserted_at = self.add_to(scanned, (new_r, self.height[new_r]))
        possible_l = [idx_height[0] for idx_height in scanned[inserted_at:]]
        l = min(possible_l)
        new_max_water = self.cal_water_simple(l, new_r)
        return l, new_max_water