public class Solution {
    public int singleNumber(int[] A) {
        int res = 0;
        for (int number: A){
            res ^= number;
        }
        return res;
    }
}