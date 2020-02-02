package main.java.code;

import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<String, Boolean> memo = new HashMap<>();

    public int removePalindromeSub(String s) {
        if (s.length() <= 1) {
            return s.length();
        }
        if (isP(s)) {
            return 1;
        } else {
            return 2;
        }
    }

    private boolean isP(String s) {
        if (s.isEmpty()) return true;
        if (memo.containsKey(s)) {
            return memo.get(s);
        }

        for (int i = 0; 2 * i < s.length() - 1; i++) {
            if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                memo.put(s, false);
                return false;
            }
        }
        memo.put(s, true);
        return true;
    }
}
