from collections import OrderedDict
class LRUCache(OrderedDict):
  def get(self, key):
    if key not in self:
      raise KeyError
    else:
      val = self[key]
      self.move_to_end(key)
      return val

  def add(self, key, value):
    if key in self:
      self.move_to_end(key)
    # add or fresh the key value
    self[key] = value

  def evict(self):
    if len(self.keys()) > 0:
      self.popitem(last=False)

  def remove(self, key):
    if key in self:
      val = self.pop(key)
      return val
    else:
      raise KeyError

def process(line):
  ops = line.rstrip().split(' ')
  if ops[0] == "add":
    key, value = ops[1], ops[2]
    cache.add(key, value)
  elif ops[0] == "get":
    key = ops[1]
    try:
      value = cache.get(key)
      print(value)
    except KeyError:
      print(-1)
  elif ops[0] == "remove":
    key = ops[1]
    try:
      value = cache.remove(key)
      print(value)
    except KeyError:
      print(-1)
  elif ops[0] == "evict":
    cache.evict()

