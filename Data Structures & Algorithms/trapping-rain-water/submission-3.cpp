class Solution {
public:
    int trap(vector<int>& height) {
        int k = 0, p=0, result=0;
        int n = height.size();
        vector<int> max_left(n);
        vector<int> max_right(n);

        for(int i=0; i< n; i++){
            k = max(k, height[i]);
            max_left[i] = k;
        }

        for(int i= n-1; i >= 0; i--){
            p = max(p, height[i]);
            max_right[i] = p;
        }

        for(int i=0; i< n; i++){
            result += min(max_left[i], max_right[i]) - height[i];
        }

        return result;

    }
};
