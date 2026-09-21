class Solution {
public:
    int maxArea(vector<int>& heights) {
        int w=0, h=0;
        int area =0;
        for(int i=0; i< heights.size(); i++){
            for(int j=i+1; j< heights.size(); j++){
                w = j - i;
                h = min(heights[i],heights[j]);
                area = max(area, w*h);
            }
        }

        return area;
    }
};
