
//TC-O(N) SC-O(1)
public class MaxConsecutiveOnesIII {
    public int longestOnes(int[] nums, int k) {
        int left = 0;         // Left pointer of the sliding window
        int maxLength = 0;    // Stores the maximum length found
        int zeroCount = 0;    // Counts the number of zeros in the current window

        // Iterate over the array with the right pointer
        for (int right = 0; right < nums.length; ++right) {
            // If the current element is 0, increment the zero count
            if (nums[right] == 0) {
                zeroCount++;
            }

            // If there are more than k zeros, shrink the window from the left
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--; // Decrease zero count as we move past a 0
                }
                left++; // Move the left pointer to shrink the window
            }

            // Update the maximum length of the window that satisfies the condition
            maxLength = Math.max(maxLength, right - left + 1);
        }

        // Return the maximum length found
        return maxLength;
    }
}
