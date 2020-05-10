import java.lang.reflect.Array;
import java.util.Arrays;

class Solution {
  public int maxNumberOfFamilies(int n, int[][] reservedSeats) {
    boolean[][] state = new boolean[n][3]; // available at left, right, middle
    for (boolean[] s : state) {
      Arrays.fill(s, true);
    }
    int row, col;
    for (int[] reservedSeat : reservedSeats) {
      row = reservedSeat[0] - 1;
      col = reservedSeat[1];
      switch (col) {
        case 2:
        case 3:
          state[row][0] = false;
          break;
        case 8:
        case 9:
          state[row][1] = false;
          break;
        case 4:
        case 5:
          state[row][0] = false;
          state[row][2] = false;
          break;
        case 6:
        case 7:
          state[row][1] = false;
          state[row][2] = false;
          break;
        default:
          break;
      }
    }
    int cnt = 0;
    for (boolean[] rowState : state) {
      if (rowState[0] && rowState[1]) {
        cnt += 2;
        continue;
      }
      if (rowState[0] || rowState[1] || rowState[2]) cnt++;
    }
    System.out.println(Arrays.deepToString(state));
    return cnt;
  }
}
