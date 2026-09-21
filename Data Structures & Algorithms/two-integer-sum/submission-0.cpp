class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int k=0;
        vector<int> nums1;
        for(int i=0; i< nums.size(); i++){
            k= target - nums[i];

            for(int j=i+1; j< nums.size(); j++){
                if(k== nums[j]){
                    nums1.push_back(i);
                    nums1.push_back(j);
                }
            }
        }

        return nums1;
    }
};
