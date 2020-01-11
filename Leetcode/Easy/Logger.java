package cpp.atcoder;

import java.util.HashMap;
import java.util.Map;

class Logger {
    Map<String, Integer> arrivalTime;

    /** Initialize your data structure here. */
    public Logger() {
        arrivalTime = new HashMap();
        
    }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    public boolean shouldPrintMessage(int timestamp, String message) {
        int last = arrivalTime.getOrDefault(message, -1);
        if (last < 0){
            arrivalTime.put(message, timestamp + 10);
            return True;
        }
        if (last <= timestamp){
            arrivalTime.put(message, timestamp + 10);
            return True;
        }
        return False;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */