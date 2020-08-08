import javax.swing.*;
import java.lang.reflect.Array;
import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Main {
  static class Pair {
    int num;
    int cut;

    Pair(int num, int cut) {
      this.num = num;
      this.cut = cut;
    }

    double getVal() {
      return -num / (double) cut;
    }
  }

  public static void main(String[] args) throws IOException {
    sc = new MScanner(System.in);
    pw = new PrintWriter(System.out);
    int N = sc.nextInt();
    int Q = sc.nextInt();
    int[] cs = sc.intArr(N);
    int[] res = new int[Q];
    int[] validNumIdx = new int[N + 1];

    List<List<Integer>> queries = new ArrayList<>();
    for (int i = 0; i < Q; i++) {
      queries.add(List.of(sc.nextInt() - 1, sc.nextInt() - 1, i));
    }
    // using right.
    queries.sort(Comparator.comparingInt(list -> list.get(1)));
    pw.println(queries.toString());
    FenwickTree fTree = new FenwickTree(N);
    int idx = 0;
    for (List<Integer> query : queries) {
     while (idx < query.get(1)) {
        // already see this key
        if (validNumIdx[cs[idx]] != 0) {
          fTree.updateElement(validNumIdx[cs[idx]] + 1, -1);
        }
        fTree.updateElement(idx + 1, 1);
        validNumIdx[cs[idx]] = idx;
        idx++;
      }
      pw.println(fTree.toString());
      long sum =
          fTree.queryRangeSumFromZeroTo(query.get(1) + 1)
              - fTree.queryRangeSumFromZeroTo(query.get(0) );
      res[query.get(2)] = (int) sum;
    }

    for (int i = 0; i < Q; i++) {
      pw.println(res[i]);
    }
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
 
