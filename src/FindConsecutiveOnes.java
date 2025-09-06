//time complexity- O(len)
//space complexity- O(len)
public class FindConsecutiveOnes {
    static int longestOnes(int[] nums, int k) {
        int len = nums.length;
        int l = 0, r = 0;
        int count = 0;

        while(r < len) {
            if(nums[r] == 0) count++;
            if(count > k) {
                if(nums[l] == 0) count--;
                l++;
            }
            r++;
        }

        return r - l;
    }
    public static void main(String[] args) {

    }
}
