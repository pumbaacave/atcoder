import java.util.*;

class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        Map<Integer, List<Integer>> subByMan = new HashMap<>();
        int man;
        for (int i = 0; i < manager.length; i++) {
            man = manager[i];
            subByMan.computeIfAbsent(man, key -> new ArrayList<>()).add(i);
        }
        return DFS(subByMan, informTime, 0, headID);
    }

    int DFS(Map<Integer, List<Integer>> subByMan, int[] informTime, int now, int man) {
        if (!subByMan.containsKey(man)) {
            return now;
        }
        int max = now;
        for (int subMan : subByMan.get(man)) {
            max = Math.max(max, this.DFS(subByMan, informTime, now + informTime[man], subMan));
        }
        return max;
        //return subByMan.get(man).stream().
        //        map(subMan -> this.DFS(subByMan, informTime, now + informTime[man], subMan)).reduce(Math::max).get();
    }
}