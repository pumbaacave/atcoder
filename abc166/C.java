import java.util.*;
import java.io.*;

public class Main {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        pw = new PrintWriter(System.out);
        // height: index
        int n = scan.nextInt();
        int[] hs = new int[n];
        boolean[] hasNei = new boolean[n];
        Arrays.fill(hasNei, false);
        boolean[] isBad = new boolean[n];
        Arrays.fill(isBad, false);
        int nEdge = scan.nextInt();
        for (int i = 0; i < n; i++) {
            hs[i] = scan.nextInt();
        }
        for (int i = 0; i < nEdge; i++) {
            int l = scan.nextInt();
            int r = scan.nextInt();
            hasNei[l - 1] = true;
            hasNei[r - 1] = true;
            if (hs[l - 1] >= hs[r - 1]) {
                isBad[r - 1] = true;
            }
            if (hs[l - 1] <= hs[r - 1]) {
                isBad[l - 1] = true;
            }

        }
        scan.close();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (!hasNei[i]) {
                cnt++;
                continue;
            }

            if (!isBad[i]) {
                cnt++;
            }
        }

        pw .println(cnt);
        pw.flush();
    }
    static PrintWriter pw;
    static MScanner  sc;
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
            while (st == null || !st.hasMoreTokens())
                st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }
        public int[] intArr(int n) throws IOException {
            int[]in=new int[n];for(int i=0;i<n;i++)in[i]=nextInt();
            return in;
        }
        public long[] longArr(int n) throws IOException {
            long[]in=new long[n];for(int i=0;i<n;i++)in[i]=nextLong();
            return in;
        }
        public int[] intSortedArr(int n) throws IOException {
            int[]in=new int[n];for(int i=0;i<n;i++)in[i]=nextInt();
            shuffle(in);
            Arrays.sort(in);
            return in;
        }
        public long[] longSortedArr(int n) throws IOException {
            long[]in=new long[n];for(int i=0;i<n;i++)in[i]=nextLong();
            shuffle(in);
            Arrays.sort(in);
            return in;
        }
        public Integer[] IntegerArr(int n) throws IOException {
            Integer[]in=new Integer[n];for(int i=0;i<n;i++)in[i]=nextInt();
            return in;
        }
        public Long[] LongArr(int n) throws IOException {
            Long[]in=new Long[n];for(int i=0;i<n;i++)in[i]=nextLong();
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
    static void shuffle(int[]in) {
        for(int i=0;i<in.length;i++) {
            int idx=(int)(Math.random()*in.length);
            int tmp=in[i];
            in[i]=in[idx];
            in[idx]=tmp;
        }
    }
    static void shuffle(long[]in) {
        for(int i=0;i<in.length;i++) {
            int idx=(int)(Math.random()*in.length);
            long tmp=in[i];
            in[i]=in[idx];
            in[idx]=tmp;
        }
    }
}



