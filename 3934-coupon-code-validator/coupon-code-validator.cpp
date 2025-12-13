class Solution {
public:
    // Helper function to check if the coupon code is valid
    bool checkValidCode(const string &s) {
        if (s.empty()) return false;

        for (char c : s) {
            if (!isalnum(c) && c != '_') {
                return false;
            }
        }
        return true;
    }

    vector<string> validateCoupons(vector<string>& code,
                                   vector<string>& businessLine,
                                   vector<bool>& isActive) {
        
        // Business line priority mapping
        unordered_map<string, int> mp = {
            {"electronics", 0},
            {"grocery", 1},
            {"pharmacy", 2},
            {"restaurant", 3}
        };

        vector<pair<int, string>> temp;

        // Filter valid coupons
        for (int i = 0; i < code.size(); i++) {
            if (isActive[i] &&
                mp.count(businessLine[i]) &&
                checkValidCode(code[i])) {

                temp.push_back({mp[businessLine[i]], code[i]});
            }
        }

        // Sort by business line priority, then by code
        sort(temp.begin(), temp.end());

        // Extract only coupon codes
        vector<string> result;
        for (auto &p : temp) {
            result.push_back(p.second);
        }

        return result;
    }
};