class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> check;

        for(int i=0; i< nums.size(); i++){
            if(find(check.begin(), check.end(), nums[i]) != check.end()){
                return true;
            }
            else{
                check.insert(nums[i]);
            }
        }

        return false;
    }
};