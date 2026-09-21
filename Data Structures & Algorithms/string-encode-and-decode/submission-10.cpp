class Solution {
public:

    string encode(vector<string>& strs) {
        string enc = "";
        for(string x: strs){
            enc += x;
            enc += "]";
        }
        return enc;
    }

    vector<string> decode(string s) {
        vector<string> result;
        string p = "";
        for(int i=0; i< s.size(); i++ ){
            if(s[i] == ']'){
                result.push_back(p);
                p = "";
                continue;
            }
            p += s[i];
            
        }
        return result;
    }
};