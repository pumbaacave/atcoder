import javax.swing.*;
import java.util.*;

class Solution {
  class Tuple {
    int left;
    double right;

    Tuple(int l, double r) {
      this.left = l;
      this.right = r;
    }

    // key building
    double getRight() {
      return -right;
    }
  }

  public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
    PriorityQueue<Tuple> queue = new PriorityQueue<>(Comparator.comparing(Tuple::getRight));
    Set<Integer> seen = new HashSet<>();
    Map<Integer, Set<Tuple>> neigh = new HashMap<>();
    for (int i = 0; i < edges.length; i++) {
      neigh.computeIfAbsent(edges[i][0], k -> new HashSet<>());
      neigh.get(edges[i][0]).add(new Tuple(edges[i][1], succProb[i]));
      neigh.computeIfAbsent(edges[i][1], k -> new HashSet<>());
      neigh.get(edges[i][1]).add(new Tuple(edges[i][0], succProb[i]));
    }
    queue.add(new Tuple(start, 1));
    while (!queue.isEmpty()) {
      Tuple cur = queue.poll();
      if (seen.contains(cur.left)) {
        contnue;
      }
      if (cur.left == end) {
        return cur.right;
      }
      if (neigh.containsKey(cur.left)) {
        neigh
            .get(cur.left)
            .forEach(tuple -> queue.offer(new Tuple(tuple.left, tuple.right * cur.right)));
      }
      seen.add(cur.left);
    }
    return 0;
  }
}
i
