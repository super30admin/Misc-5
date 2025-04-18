// TC: O(n)
// SC: O(n)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No


public class Solution {
    
    // Function to remove all continuous characters (groups) whose count is 3 or more.
    public String removeContinuous(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        
        // Use a stack that stores pairs: (character, current contiguous count)
        Stack<Pair> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek().ch == c) {
                stack.peek().count++;
                // If the current group reaches 3 or more, remove it.
                if (stack.peek().count >= 3) {
                    stack.pop();
                }
            } else {
                stack.push(new Pair(c, 1));
            }
        }
        
        // Reconstruct the string from the stack.
        StringBuilder sb = new StringBuilder();
        for (Pair p : stack) {
            for (int i = 0; i < p.count; i++) {
                sb.append(p.ch);
            }
        }
        
        return sb.toString();
    }
    
    private static class Pair {
        char ch;
        int count;
        
        Pair(char ch, int count) {
            this.ch = ch;
            this.count = count;
        }
    }