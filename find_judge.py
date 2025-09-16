class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> given(n+1, 0);
        vector<int> received(n+1, 0);
        
        for (const auto& t : trust) {
            given[t[0]] = given[t[0]] + 1;
            received[t[1]] = received[t[1]] + 1;
        } // <-- This closing brace was missing
        
        for (int i = 1; i <= n; i++) {
            if (given[i] == 0 && received[i] == n-1) {
                return i;
            }
        }
        
        return -1;
    }
};
