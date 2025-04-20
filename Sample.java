class Sample{
/**************************PROBLEM-1*******************/
    //TC:0(N*N)
//SC:0(N)
    class Solution {
        public String removeDuplicates(String s, int k) {
            if(s==null || s.length()==0){
                return null;
            }
            Stack<Integer> st=new Stack<>();
            StringBuilder sb=new StringBuilder(s);
            for(int i=0;i<sb.length();i++){
                char c=sb.charAt(i);
                if(st.isEmpty() || (c!=sb.charAt(i-1))){
                    st.push(1);
                }else{
                    int value=st.pop();
                    if(value+1==k){
                        sb.delete(i-k+1,i+1);
                        i=i-k;
                    }else{
                        st.push(value+1);
                    }
                }
            }
            return sb.toString();
        }
    }
/**************************PROBLEM-2*******************/
}