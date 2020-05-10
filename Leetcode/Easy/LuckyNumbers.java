import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> luckyNumbers(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        List<Integer> ret = new ArrayList<>();
        int val;
        ounter:
        for (int i = 0; i < m; i++) {
            int c = 0, rowMin = 1000000;
            for (int j = 0; j < n; j++) {
                val = matrix[i][j];

                if (val < rowMin) {
                    rowMin = val;
                    c = j;
                }
            }
            for (int k = 0; k < m; k++) {
                if (matrix[k][c] > rowMin) {
                    continue ounter;
                }
            }
            ret.add(rowMin);
        }
        return ret;
    }
}