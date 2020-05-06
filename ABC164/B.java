import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        int d = scan.nextInt();
        scan.close();

        String message = turn(a,d) >= turn(c, b) ? "Yes" : "No";
        System.out.println(message);
    }
    static int turn(int hp, int atk) {
        return hp / atk + (hp % atk == 0 ? 0 : 1);
    }
}

