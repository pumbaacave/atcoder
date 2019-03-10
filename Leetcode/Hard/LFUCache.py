from collections import OrderedDict, defaultdict
class LFUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.key_freq = {}
        self.key_val = {}
        # for LRU tie breaking
        self.freq_key = defaultdict(OrderedDict)
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.key_val:
            val = self.key_val[key]
            # get and update the frequecy
            freq = self.key_freq[key]
            self.key_freq[key] += 1
            # move to upper freq dict
            del self.freq_key[freq][key]
            self.freq_key[freq + 1][key] = val
            print(self.key_val)
            print(self.key_freq)
            print(self.freq_key)

            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        """
        if there is a tie
        the least recetly used key would be evited
        """
        if self.capacity == 0:
            return

        if key in self.key_val:
            # update key frequency
            freq = self.key_freq[key]
            self.key_freq[key] += 1
            # move to upper freq dict
            del self.freq_key[freq][key]
            self.insert_to_freq_key(freq + 1, key, value)
            # update value
            self.key_val[key] = value

        else:
            if len(self.key_val) < self.capacity:
                self.insert_new_value(key, value)
            else:
                f = self.least_freq()
                # delete LFU key
                e_key, _ = self.freq_key[f].popitem(last=False)
                del self.key_freq[e_key]
                del self.key_val[e_key]
                self.insert_new_value(key, value)

        print(self.key_val)
        print(self.key_freq)
        print(self.freq_key)

    def insert_new_value(self, key, value):
        self.key_val[key] = value
        self.insert_to_freq_key(1, key, value)
        self.key_freq[key] = 1

    def least_freq(self):
        """
        return frequency of least non-emplty frequency_key_dict
        """
        freqs = sorted(self.freq_key.keys())
        for f in freqs:
            if self.freq_key[f]:
                return f

    def insert_to_freq_key(self, freq, key, value):
        self.freq_key[freq][key] = value
        self.freq_key[freq].move_to_end(key)



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
def test_zero_cap():
    c = LFUCache(0)
    c.put(0, 0)
    assert c.get(0) == -1

def test_put():
    c = LFUCache(2)
    c.put(1, 1)
    c.put(1, 1)
    c.put(1, 1)
    assert c.key_freq[1] == 3, "WRONG FREQ"
    c.put(1, 2)
    assert c.key_freq[1] == 4, "WRONG FREQ"
    assert c.get(1) == 2
    assert c.key_freq[1] == 5, "WRONG FREQ"
    assert not c.freq_key[1], "NOT EMPTY"
    assert not c.freq_key[2], "NOT EMPTY"
    assert not c.freq_key[3], "NOT EMPTY"
    assert not c.freq_key[4], "NOT EMPTY"
    assert c.freq_key[5], "SHOULD BE EMPTY"
    print(c.freq_key)

def est_cache():
    c = LFUCache(2)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    assert c.get(3) == 3
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4
