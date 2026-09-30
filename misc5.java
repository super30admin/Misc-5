//problem1
class Solution {
    public int longestOnes(int[] nums, int k) {
        int n=nums.length;
        int slow=0;
        for(int i=0;i<n;i++){
            if(nums[i]==0) k--;
            if(k<0){
                if(nums[slow]==0) k++;
                slow++;
            }
        }
        return n-slow;
    }
}
//problem2
class Main {
    public static void main(String[] args) {
        String s = "abbacccaa";
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            char ch = s.charAt(i);
            int count = 0;
            // Count current continuous group
            while (i < s.length() && s.charAt(i) == ch) {
                count++;
                i++;
            }
            // Keep it only if count <= 2
            if (count <= 2) {
                for (int j = 0; j < count; j++) {
                    sb.append(ch);
                }
            }
        }
        System.out.println(sb);
    }
}
