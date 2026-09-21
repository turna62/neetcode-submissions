class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int longest = 0;

        for(int x : nums){
            int count =0, curr = x;
            while(numSet.find(curr) != numSet.end()){
                count++;
                curr++;
            }

            longest = max(longest, count);
        }

        return longest;

    }

};
