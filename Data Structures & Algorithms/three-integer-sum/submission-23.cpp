class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;

        for(int l=0; l < nums.size()-1; l++){

        int l1 = l+1; int r=nums.size()-1;

        while(l1 < r){

            int sum = nums[l]+nums[l1]+nums[r];

            if(sum < 0){
                l1++;
            }
            
            else if(sum > 0){
                r--;
            }

            else{
                vector<int> temp = {nums[l], nums[l1], nums[r]};
                auto it = find(result.begin(), result.end(), temp);
                if (it == result.end()){
                result.push_back({nums[l], nums[l1], nums[r]});
                }
                l1++;
                r--;
            }
        }

        }

        return result;

    }
};
