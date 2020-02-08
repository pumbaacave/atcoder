package main.java.code;

import java.util.Arrays;

class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if(n < d){
            return -1;
        }
        // skip dp
        if(n == d){
            int sum = 0;
            for(int job: jobDifficulty){
                sum += job;
            }
            return sum;
        }

        // state[i][j] :== min difficulty for j jobs assign to i days
        int[][] state = new int[d][n];
        int[][] map = new int[n][n];

        for (int start = 0; start < n; start++) {
            for (int end = start; end < n; end++) {
                if (start == end){
                    map[start][end] = jobDifficulty[start];
                    continue;
                }
                map[start][end] = Math.max(map[start][end - 1], jobDifficulty[end]);
            }
        }
        // initialize
        state[0][0] = jobDifficulty[0];
        for (int i = 1; i < n; i++) {
            state[0][i] = Integer.max(state[0][i-1], jobDifficulty[i]);
        }

        for (int i = 1; i < d; i++) {
            for (int j = 0; j < n; j++) {
                state[i][j] = Integer.MAX_VALUE;
            }
        }

        // separate to i days
        for(int i = 1; i < d; i ++){
            // iterate till j-th job, but numDays > numJobs
            for (int jobNum = i; jobNum < n; jobNum++) {
                //update state[i][jobNum] using best result from i-1 th days result
                for (int j = i - 1; j < jobNum; j++) {
                    state[i][jobNum] = Math.min(state[i][jobNum],
                            state[i-1][j] + map[j+1][jobNum]);
                }
            }
        }
        //System.out.println(Arrays.deepToString(state));
        return state[d-1][n-1];
    }
}