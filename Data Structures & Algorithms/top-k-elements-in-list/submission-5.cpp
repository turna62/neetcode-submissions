class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k){

        unordered_map<int, int> mp;
        int count =1;
        sort(nums.begin(), nums.end());

        for(int num : nums){
            mp[num]++;
        }

        vector<int> result;
        vector<pair<int, int>> vec(mp.begin(), mp.end());
        sort(vec.begin(), vec.end(), [](pair<int,int> &a, pair<int,int> &b){
                return a.second > b.second; 
            });


        for(int i=0; i < k; i++){
            result.push_back(vec[i].first);
        }

        return result;

    }
};   