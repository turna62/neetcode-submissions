class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        for(int i=0; i< nums.size(); i++){
            for(int j=1; j< nums.size(); j++){
                if(target == nums[i] + nums[j]){
                    result.push_back(i + 1);
                    result.push_back(j + 1);
                    return result;
                }
            }
        }
        return result;
    }
};
