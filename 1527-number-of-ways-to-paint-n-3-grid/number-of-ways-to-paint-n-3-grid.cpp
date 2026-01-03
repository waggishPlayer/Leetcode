class Solution {
public:
    int numOfWays(int n) {
        long long MOD = 1e9 + 7;
        long long aba = 6;
        long long abc = 6;

        for (int i = 2; i <= n; i++) {
            long long prev_aba = aba;
            long long prev_abc = abc;
            aba = (prev_aba * 3 + prev_abc * 2) % MOD;
            abc = (prev_aba * 2 + prev_abc * 2) % MOD;
        }
        return (aba + abc) % MOD;
    }
};