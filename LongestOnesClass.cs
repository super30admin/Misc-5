public class Solution {
    // TC => O(n)
    // SC => O(1)
    public int LongestOnes(int[] nums, int k) {
        if(nums == null || nums.Length == 0){
            return 0;
        }

        int n = nums.Length;
        int left = 0;
        for(int i = 0; i < n; i++){
            if(nums[i] == 0){
                k--;
            }
            if(k < 0){
                if(nums[left] == 0){
                    k++;
                }
                left++;
            }
        }

        return n - left;
    }
}