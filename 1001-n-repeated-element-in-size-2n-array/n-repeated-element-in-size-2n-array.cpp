class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_set<int> bag;

        for (int num:nums){
            if(bag.count(num)){
                return num;
            }
            bag.insert(num);
        }
        return 0;
    }
};