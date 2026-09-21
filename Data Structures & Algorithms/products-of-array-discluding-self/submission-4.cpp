class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> suffix(n);
        vector<int> preffix(n);
        vector<int> result(n);

        preffix[0] = 1;
        suffix[n-1] = 1;

        for (int i = 1; i < n; i++){
            preffix[i] = nums[i-1] * preffix[i-1];
        } 

        for (int i = n-2; i >=0; i--){
            suffix[i] = nums[i+1] * suffix[i+1];
        }

        for (int i = 0; i < n; i++){
            result[i] = suffix[i] * preffix[i];
        } 

        return result;

    }
};
