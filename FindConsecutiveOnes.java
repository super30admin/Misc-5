// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

// Your code here along with comments explaining your approach
/*
We go through the input array and count number of zeroes seen so far. Once it exceeds k value, we form a sliding
window where we move the left pointer and adjust the countZero variable until it reaches back to k value.At
every stage we compute the max length of the sliding window formed and return it at last.
 */
class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int countZero = 0;
        int maxLength = 0;
        for(int right = 0 ; right < nums.length ; right++) {
            if(nums[right] == 0)
                countZero++;
            while(countZero > k) {
                if(nums[left] == 0)
                    countZero--;
                left++;
            }
            maxLength = Math.max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}
