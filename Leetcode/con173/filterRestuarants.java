package main.java.code;

import java.util.*;

class Solution {
    private static class Pair implements Comparable<Pair> {
        int f;
        int s;

        Pair(int f, int s) {
            Pair.this.f = f;
            Pair.this.s = s;
        }

        @Override
        public int compareTo(Pair o) {
            if (f == o.f) {
                return -Integer.compare(s, o.s);
            }
            return -Integer.compare(f, o.f);
        }

        @Override
        public String toString() {
            return String.valueOf(f) + ": " + String.valueOf(s);
        }
    }

    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        if (restaurants.length == 0) {
            return Collections.emptyList();
        }
        SortedSet<Pair> rateById = new TreeSet<>();
        for (int i = 0; i < restaurants.length; i++) {
            if ((restaurants[i][2] >= veganFriendly) && (restaurants[i][3] <= maxPrice) && (restaurants[i][4] <= maxDistance)) {
                Pair p = new Pair(restaurants[i][1], restaurants[i][0]);
                rateById.add(p);
            }
        }
        List<Integer> ret = new ArrayList<>();
        for (Pair p : rateById) {
            ret.add(p.s);
        }
        return ret;
    }
}
