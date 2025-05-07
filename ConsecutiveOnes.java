class Solution {
    public int longestOnes(int[] nums, int k) {
        int slow = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == 0){
               k--;
            }
            if(k < 0){
                if(nums[slow] == 0) k++;
                slow++;
            }
        }
        return nums.length - slow;
    }
}