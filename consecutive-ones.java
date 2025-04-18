// TC: O(n)
// SC: O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

public int consecutiveOnes(int[] A, int K) {
    int i = 0, j;
    for (j = 0; j < A.length; ++j) {
        if (A[j] == 0) K--;
        if (K < 0 && A[i++] == 0) K++;
    }
    return j - i;
}