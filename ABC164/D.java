import java.text.ParseException;
import java.util.*;

public class Main {
    // half right
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<Integer> intList = new ArrayList<>();
        String n = scan.nextLine();
        scan.close();
        for (int i = 0; i < n.length(); i ++){
            intList.add(n.charAt(i) - '0');
        }

        if (intList.size() < 4) {
            System.out.println(0);
        }
        int cnt = 0;
        for (int i = 0; i < intList.size() - 4; i++) {
            int tmp = intList.get(i) * 100 + intList.get(i + 1) * 10 + intList.get(i + 2);
            for (int j = i + 3; j < intList.size(); j++) {
                tmp = tmp * 10 + intList.get(j);
                if (tmp == 0) {
                    continue;
                }
                tmp = tmp % 2019;
                if (tmp == 0) {
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
}

