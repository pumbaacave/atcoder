import java.util.*;
import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException {
    sc = new MScanner(System.in);
    pw = new PrintWriter(System.out);
    int H = sc.nextInt();
    int W = sc.nextInt();
    int K = sc.nextInt();
    char[][] array = new char[H][W];

    // bit mask
     for (int i = 0; i < H; i++) {
      array[i] = sc.nextLine().toCharArray();
    //  pw.println(Arrays.toString(array[i]));
     }

    // Backtracking
    int cnt = 0;
    for (int i = 0; i < Math.pow(2, H); i++) {
      for (int j = 0; j < Math.pow(2, W); j++) {
        if (check(array, i, j, H, W) == K) {
          cnt++;
        }
      }
    }
    pw.println(cnt);
    pw.flush();
  }

  static int check(char[][] array, int rM, int cM, int H, int W) {
    int cnt = 0;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (array[i][j] == '#' && (((rM >> i) & 1) == 0) && (((cM >> j) & 1) == 0)) {
          cnt++;
        }
      }
    }
    //System.out.println(rM);
    //System.out.println(cM);
    //System.out.println(cnt);
    return cnt;
  }

  // sc.close();
  // pw.println(cnt);
  // pw.flush();
  public static int cal(int flipped) {
    int cnt = 0;
    while (flipped != 0) {
      flipped = flipped % numPop(flipped);
      cnt++;
    }
    return cnt;
  }

  public static int numPop(int num) {
    int cnt = 0;
    while (num != 0) {
      cnt += (num & 1);
      num = num >> 1;
    }
    return cnt;
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

