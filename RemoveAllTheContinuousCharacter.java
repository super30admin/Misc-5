// Time Complexity : O(n)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

// Your code here along with comments explaining your approach
/*
We iterate through the input string and push characters and their respective frequencies into 2 separate
stacks.While computing the frequency, we check if its equal to k, if so, we pop the character and number stacks.
If not, we continue to push. Lastly, we build the string with the remaining characters in the char stack along
with their frequencies in the number stack and reverse it before returning to comply with the LIFO principle and
our expected output.
 */
class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<Character> charStack = new Stack<>();
        Stack<Integer> numStack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        for(char ch : s.toCharArray()) {
            if(!charStack.isEmpty() && ch == charStack.peek()) {
                int frq = numStack.pop();
                frq++;

                if(frq == k) {
                    charStack.pop();
                }
                else {
                    numStack.push(frq);
                }
            }
            else {
                charStack.push(ch);
                numStack.push(1);
            }
        }

        while(!charStack.isEmpty()) {
            char ch = charStack.pop();
            int frq = numStack.pop();

            for(int i = 0 ; i < frq ; i++)
                sb.append(ch);
        }
        return sb.reverse().toString();
    }
}