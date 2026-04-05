class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = size(nums);
        vector<int>ans(n*2);

        for (int num = 0; num<n; num++){
            ans[num] = nums[num];
            ans[num+n] = nums[num];
        }
        return ans;
    }
};