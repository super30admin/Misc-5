class Solution {
    public int longestOnes(int[] nums, int k) {

        if (nums == null || nums.length == 0) {
            return 0;
        }

        int start = 0, end = 0, count = 0;

        int max = -1;
        while (end < nums.length) {
            
            if (nums[end] == 0) {
                count++;
            }

            // reduce number of 0 (move start pointer) when count > k
            while (count > k) {
                if (nums[start] == 0) {
                    count--;
                }
                start++;
            }

            max = Math.max(max, end - start + 1);
            end++;
        }

        return max;
        
    }
}