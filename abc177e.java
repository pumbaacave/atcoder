import java.io.*;
import java.util.*;

public class Main {
  static class Pair {
    int num;
    int cut;

    Pair(int num, int cut) {
      this.num = num;
      this.cut = cut;
    }
  }

  static int gcd(int a, int b) {
    while (b != 0) {
      int temp = a % b;
      a = b;
      b = temp;
    }
    return a;
  }

  // static Map<String, Long> memo = new HashMap<>();

  public static void main(String[] args) throws IOException {
    sc = new MScanner(System.in);
    pw = new PrintWriter(System.out);
    int N = sc.nextInt();
    int[] nums = sc.intArr(N);
    int max = 1000009;
    int[] memo = new int[max];
    for (int num : nums) {
      memo[num]++;
    }
    boolean pairwise = true;
    Head:
    for (int i = 2; i < max; i++) {
      int cnt = 0;
      for (int j = i; j < max; j += i) {
        cnt += memo[j];
        if (cnt > 1) {
          pairwise = false;
          break Head;
        }
      }
    }
    if (pairwise) {
      pw.println("pairwise coprime");
      pw.flush();
      return;
    }
    // pw.println(Arrays.toString(memo));
    // pw.println(seen);

    boolean setPrime = false;
    int cur = nums[0];
    for (int i = 0; i < N; i++) {
      cur = gcd(cur, nums[i]);
      if (cur == 1) {
        setPrime = true;
        break;
      }
    }

    if (setPrime) {
      pw.println("setwise coprime");
    } else {
      pw.println("not coprime");
    }

    // pw.println(groupsSizeCount.entrySet());
    // pw.println(m);
    // pw.println();

    pw.flush();
    // System.out.println(cnt);
  }

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

  // sc.close();
  // pw.println(cnt);
  // pw.flush();

  static PrintWriter pw;
  static MScanner sc;

  static class MScanner {
    StringTokenizer st;
    BufferedReader br;

    public MScanner(InputStream system) {
      br = new BufferedReader(new InputStreamReader(system));
    }

    public MScanner(String file) throws Exception {
      br = new BufferedReader(new FileReader(file));
    }

    public String next() throws IOException {
      while (st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
      return st.nextToken();
    }

    public int[] intArr(int n) throws IOException {
      int[] in = new int[n];
      for (int i = 0; i < n; i++) in[i] = nextInt();
      return in;
    }

    public long[] longArr(int n) throws IOException {
      long[] in = new long[n];
      for (int i = 0; i < n; i++) in[i] = nextLong();
      return in;
    }

    public int[] intSortedArr(int n) throws IOException {
      int[] in = new int[n];
      for (int i = 0; i < n; i++) in[i] = nextInt();
      shuffle(in);
      Arrays.sort(in);
      return in;
    }

    public long[] longSortedArr(int n) throws IOException {
      long[] in = new long[n];
      for (int i = 0; i < n; i++) in[i] = nextLong();
      shuffle(in);
      Arrays.sort(in);
      return in;
    }

    public Integer[] IntegerArr(int n) throws IOException {
      Integer[] in = new Integer[n];
      for (int i = 0; i < n; i++) in[i] = nextInt();
      return in;
    }

    public Long[] LongArr(int n) throws IOException {
      Long[] in = new Long[n];
      for (int i = 0; i < n; i++) in[i] = nextLong();
      return in;
    }

    public String nextLine() throws IOException {
      return br.readLine();
    }

    public int nextInt() throws IOException {
      return Integer.parseInt(next());
    }

    public double nextDouble() throws IOException {
      return Double.parseDouble(next());
    }

    public char nextChar() throws IOException {
      return next().charAt(0);
    }

    public long nextLong() throws IOException {
      return Long.parseLong(next());
    }

    public boolean ready() throws IOException {
      return br.ready();
    }

    public void waitForInput() throws InterruptedException {
      Thread.sleep(3000);
    }
  }

  static void shuffle(int[] in) {
    for (int i = 0; i < in.length; i++) {
      int idx = (int) (Math.random() * in.length);
      int tmp = in[i];
      in[i] = in[idx];
      in[idx] = tmp;
    }
  }

  static void shuffle(long[] in) {
    for (int i = 0; i < in.length; i++) {
      int idx = (int) (Math.random() * in.length);
      long tmp = in[i];
      in[i] = in[idx];
      in[idx] = tmp;
    }
  }
}

