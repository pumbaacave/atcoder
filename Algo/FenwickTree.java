/**
 * https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree A space efficient version segment
 * tree. Usually for range sum. Or the required metric can be calulated in that:
 *
 * <p>right_metric = parant_metric - left_metric Only then, we can stop memoizing right_metric
 *
 * <p>The internal structure is a 1-base array, to simplify calculation of parent node's idx. lsb
 * = 3 & -3 = 2 (0x0011 & 0x1101 = 0x0001) lastParentOf3 = 3 - lsb = 2 curParentOf3 = 3 + lsb = 4
 */
static class FenwickTree {
  private final long[] state;
  private final int size;

  FenwickTree(int size) {
    this.size = size;
    state = new long[size + 1];
  }

  @Override
  public String toString() {
    return Arrays.toString(state);
  }

  long queryRangeSumFromZeroTo(int idx) {
    long sum = 0;
    while (idx != 0) {
      sum += state[idx];
      idx -= (idx & -idx);
    }
    return sum;
  }

  /** @param val can be negative */
  void updateElement(int idx, long val) {
    while (idx <= size) {
      state[idx] += val;
      idx += (idx & -idx);
    }
  }
}


