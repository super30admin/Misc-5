// TC: O(n)
// SC: O(1)
class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;

        int result = 0;
        int left = 0;
        int count = 0;
        for (int right = 0; right < n; right++) {

            if (nums[right] == 0) {
                count++;
            }

            if (count > k) {
                if(nums[left] == 0){
                    count--;
                }
                left++;
            }
            result = Math.max(result, right - left + 1);
        }

        return result;
    }
}