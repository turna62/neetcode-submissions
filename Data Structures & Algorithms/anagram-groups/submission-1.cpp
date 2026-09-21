class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string, vector<string>> mp;

        for(string x : strs){
            string k= x;
            sort(x.begin(), x.end());
            mp[x].push_back(k);
        }

        vector<vector<string>> result;
        for (auto &p: mp){
            result.push_back(p.second);
        }

        return result;
    }
};
