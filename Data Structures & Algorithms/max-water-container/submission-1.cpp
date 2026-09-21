class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l=0, r = heights.size()-1;
        int area = 0;

        while(l<r){
            int w = r-l;
            int h = min(heights[l], heights[r]);
            area = max(area, w*h);

            if(heights[l]<heights[r]){
                l++;
            }
            else{
                r--;
            }
        }

        return area;
    }
};
