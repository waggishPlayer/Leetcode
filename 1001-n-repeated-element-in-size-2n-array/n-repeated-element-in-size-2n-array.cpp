class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i != j && nums[i] == nums[j]) {
                    return nums[i];
                }
            }
        }
        return 0;
    }
};