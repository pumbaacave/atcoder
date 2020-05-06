import java.util.HashSet;
        import java.util.Scanner;
        import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Set set = new HashSet<String>();
        Scanner scan = new Scanner(System.in);
        int times = scan.nextInt();
        for (int i = 0; i < times; i++) {
            set.add(scan.next());
        }
        scan.close();

        set.forEach(o ->
                System.out.println()
        );
        System.out.println(set.size());
    }
}

