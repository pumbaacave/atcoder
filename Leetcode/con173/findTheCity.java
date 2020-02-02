package main.java.code;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        int[][] distances = new int[n][n];
        for (int[] arr : distances) {
            Arrays.fill(arr, 10001);
        }
        for (int i = 0; i < n; i++) {
            distances[i][i] = 0;
        }
        for (int i = 0; i < edges.length; i++) {
            if (edges[i][2] > distanceThreshold) {
                continue;
            }
            distances[edges[i][0]][edges[i][1]] = edges[i][2];
            distances[edges[i][1]][edges[i][0]] = edges[i][2];
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    distances[i][j] = Math.min(distances[i][k] + distances[k][j], distances[i][j]);
                }
            }
        }
        int curCount, oldCount = n + 1;
        int idx = -1;
        //System.out.println(Arrays.deepToString(distances));
        for (int i = 0; i < n; i++) {
            curCount = 0;
            for (int j = 0; j < n; j++) {
                if (distances[i][j] <= distanceThreshold) {
                    curCount++;
                }
            }
            if (curCount <= oldCount) {
                idx = i;
                oldCount = curCount;
            }
        }
        return idx;
    }
}