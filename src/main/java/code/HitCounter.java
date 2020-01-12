package main.java.code;

import java.util.Deque;
import java.util.LinkedList;

class HitCounter {
    private Deque<Integer> stamps;
    private static final Integer INTERVAL = 300;

    /** Initialize your data structure here. */
    public HitCounter() {
        this.stamps = new LinkedList<>();
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        stamps.addLast(timestamp);
        while(!stamps.isEmpty() && stamps.getFirst() <= timestamp - INTERVAL){
            stamps.pollFirst();
        }
        
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        while(!stamps.isEmpty() && stamps.getFirst() <= timestamp - INTERVAL){
            stamps.pollFirst();
        }
        return stamps.size();
    }
}

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter obj = new HitCounter();
 * obj.hit(timestamp);
 * int param_2 = obj.getHits(timestamp);
 */