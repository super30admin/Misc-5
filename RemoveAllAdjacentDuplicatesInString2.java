// TC: O(n)
// SC: O(n)
class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<Character> chSt = new Stack<>();
        Stack<Integer> ctSt = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (!chSt.isEmpty() && chSt.peek() == ch) {
                int newCnt = ctSt.pop() + 1;

                if (newCnt == k) {
                    chSt.pop();
                } else {
                    ctSt.push(newCnt);
                }
            } else {
                chSt.push(ch);
                ctSt.push(1);
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!chSt.isEmpty()) {
            char ch = chSt.pop();
            int count = ctSt.pop();

            for (int i = 0; i < count; i++) {
                sb.append(ch);
            }
        }
        return sb.reverse().toString();
    }
}