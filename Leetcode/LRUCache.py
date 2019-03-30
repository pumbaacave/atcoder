from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return -1
        else:
            val = self[key]
            self.move_to_end(key)
            return val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self:
            self.move_to_end(key)

        # fresh key first
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)
