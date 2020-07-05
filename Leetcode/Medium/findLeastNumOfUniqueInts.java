import java.util.*;
import java.util.stream.Collectors;

class Solution {
  public int findLeastNumOfUniqueInts(int[] arr, int k) {
    Map<Integer, Integer> cnt = new HashMap<>();
    for (int num : arr) {
      cnt.compute(num, (key, v) -> v == null ? 1 : v + 1);
    }
    int cnts =
        cnt.values().stream()
            .sorted()
            .reduce(
                k,
                (acc, num) -> {
                  if (acc >= num) {
                    return acc - num;
                  } else {
                    return acc > 0 ? -1 : acc - 1;
                  }
                });
    return -cnts;
  }
}
