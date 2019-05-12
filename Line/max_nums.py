def mul3(a, b, c):
    return a * b * c
def process(line):
  if not line:
    return -1
  nums = list(map(int, line.split(",")))
  nums.sort()
  L = len(nums)
  if L < 3:
    return -1
  # running max
  run_max = -float("inf")
  for i in range(L-2):
      run_max = max(run_max, mul3(*nums[i:i+3]))
  # 2 negative 1 positive
  end_max = mul3(nums[0], nums[1], nums[-1])
  return max(run_max, end_max)
