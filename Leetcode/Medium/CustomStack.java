import java.util.Arrays;

class CustomStack {

    int[] stack;
    int idx;
    private static final int SIZE = 10;
    static int[] incr = new int[SIZE];

    public CustomStack(int maxSize) {
        stack = new int[maxSize];
        idx = 0;
        Arrays.fill(stack, 0);
        Arrays.fill(incr, 0);
    }

    public void push(int x) {
        if (idx < stack.length) {
            stack[idx++] = x;
        }
    }

    public int pop() {
        if (idx == 0) return -1;

        int delta = incr[idx - 1];
        incr[idx - 1] = 0;
        return stack[--idx] + delta;
    }

    public void increment(int times, int val) {
        // TODO: use delta if performance required
        int end = Math.min(idx, times);
        for (int i = 0; i < end; i++) {
            incr[i] += val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */