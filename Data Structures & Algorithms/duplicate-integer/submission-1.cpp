class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        unordered_set<int> s;
        for(int i=0; i< nums.size(); i++){
            if(s.find(nums[i]) != s.end()){
                return true;
            }

            s.insert(nums[i]);
        }

        return false;
    }
};