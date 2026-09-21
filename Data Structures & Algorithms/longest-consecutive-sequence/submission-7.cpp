class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for(int i=0; i<nums.size(); i++){
            int count = 0;
            int curr = nums[i];

            while(numSet.find(curr) != numSet.end()){
                curr++;
                count++;
            }

            longest = max(longest, count);
        }

        return longest;
    }

};
