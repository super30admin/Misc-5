import java.util.ArrayDeque;
import java.util.Deque;

public class RemoveAllAdjecentDuplicatesII {
    public String removeDuplicates(String s, int k) {
        // Stack to store characters and their counts
        Deque<Pair> stack = new ArrayDeque<>();

        for (char c : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peek().ch == c) {
                // Increment count if same character
                stack.peek().count++;
                // If count reaches k, remove the element
                if (stack.peek().count == k) {
                    stack.pop();
                }
            } else {
                // Push new character with count 1
                stack.push(new Pair(c, 1));
            }
        }

        // Reconstruct the final string
        StringBuilder sb = new StringBuilder();
        for (Pair p : stack) {
            for (int i = 0; i < p.count; i++) {
                sb.insert(0, p.ch); // insert at beginning since we used stack
            }
        }

        return sb.toString();
    }

    // Helper class to store character and count
    private static class Pair {
        char ch;
        int count;

        Pair(char ch, int count) {
            this.ch = ch;
            this.count = count;
        }
    }
}
