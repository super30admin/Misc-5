class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<Character> st = new Stack<>();
        Stack<Integer> count = new Stack<>();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(st.isEmpty() || st.peek() != c){
                st.push(c);
                count.push(1);
            } else {
               int newCnt =  count.pop() + 1;
                if(newCnt == k){
                    st.pop();
                } else{
                    count.push(newCnt);
                }
            }
        }
        StringBuilder result= new StringBuilder();
        while(!st.isEmpty()){
            char c = st.pop();
            int cnt = count.pop();
            for(int j = 0; j < cnt; j++){
                result.append(c);
            }
        }
        return result.reverse().toString();
    }
}