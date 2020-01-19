import java.util.*;

class Solution {
    public int makeConnected(int n, int[][] connections) {
        if (connections.length < n - 1) {
            return -1;
        }
        List<Integer> pars = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            pars.add(i, i);
        }
        int numGroup = n;
        for (int[] connection : connections) {
            if (unionFind(connection[0], connection[1], pars)){
                numGroup -= 1;
            }
        }

        return numGroup - 1;
    }

    private Integer findParent(Integer idx, List<Integer> pars) {
        if (pars.get(idx).equals(idx)) {
            return idx;
        }
        return findParent(pars.get(idx), pars);
    }

    private void setParent(Integer idx, List<Integer> pars, Integer newP) {
        if (!pars.get(idx).equals(idx)){
            // recur to parent first
            setParent(pars.get(idx), pars, newP);
        }
        pars.set(idx, newP);
    }


    // @return ture when union happened
    private boolean unionFind (Integer l, Integer r, List < Integer > pars){
        // same parent
        Integer lp = findParent(l, pars);
        Integer rp = findParent(r, pars);
        if (lp.equals(rp)) {
            return false;
        }
        if (lp < rp){
            setParent(r, pars, lp);
        } else {
            setParent(l, pars, rp);
        }
        return true;
    }

    }