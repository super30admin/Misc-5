class Pair {
    char c;
    int freq;
    Pair(char c, int freq) {
        this.c = c;
        this.freq = freq;
    }
}
class Solution {
    public String removeDuplicates(String s, int k) {
        if (s == null || s.length() == 0 || k == 0) {
            return s;
        }

        Stack<Pair> stack = new Stack<>();

        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            if (stack.isEmpty() || c != stack.peek().c) {
                stack.push(new Pair(c, 1));
            } else {
                Pair top = stack.pop();
                if (top.freq + 1 < k) {
                    top.freq = top.freq + 1;
                    stack.push(top);
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        for (Pair p : stack) {
            sb.append(String.valueOf(p.c).repeat(p.freq));
        }

        return sb.toString();
    }
}