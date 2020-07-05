import java.util.*;
import java.io.*;

public class Main {
  static int len;

  // sum of divisor
  public static void main(String[] args) throws IOException {
    sc = new MScanner(System.in);
    pw = new PrintWriter(System.out);
    // height: index
    int n = sc.nextInt();
    long total = 0;
    int[] nums = new int[n + 1];
    List<Integer> primes = new ArrayList<>();
    int top = (int) Math.ceil(Math.sqrt(n));
    pw.println(top);
    for (int i = 2; i <= top; i++) {
      if (isPrime(i)) {
        primes.add(i);
      }
    }
    // backtracking
      Map<Integer, Integer> counts = new HashMap<>();
    for (Integer p: primes) {
      counts.put(p, 0);
    }
    nums[1] = 1;
    dfs(primes, counts, 1, nums, n);


    for (int i = 1; i <= n; i++) {
      if(nums[i] == 0) nums[i] = 2;
      total += i * nums[i];
    }

    pw.println(primes);
    pw.println(Arrays.toString(nums));
    pw.println(total);
    pw.flush();

    // sc.close();
    // pw.println(cnt);
    // pw.flush();
  }

  private static void dfs(
      List<Integer> primes, Map<Integer, Integer> counts, int key, int[] state, int limit) {
    if (key > limit) return;
    if (key != 1 && state[key] != 0) return;
    if (key != 1) {

      state[key] = counts.values().stream().reduce(0, (integer, integer2) -> (integer +1) * (integer2 + 1));
    }
    for (Integer prime: primes) {
        counts.compute(prime, (xx, cnt) -> cnt +1);
        dfs(primes, counts, key * prime, state, limit);
      counts.compute(prime, (xx, cnt) -> cnt -1);
    }
  }

  private static boolean isPrime(int num) {
    for (int i = 2; i < num; i++) {
      if (num % i == 0) {
        return false;
      }
    }
    return true;
  }

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
