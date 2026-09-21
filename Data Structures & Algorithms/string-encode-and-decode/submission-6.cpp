class Solution {
public:

    string encode(vector<string>& strs) {
        string enc = "";
        for(string x: strs){
            enc += x;
            enc += "]";
        }
        reverse(enc.begin(), enc.end());
        return enc;
    }

    vector<string> decode(string s) {
        reverse(s.begin(), s.end());
        vector<string> result;
        string p = "";
        for(int i=0; i< s.size(); i++ ){
            if(s[i] != ']'){
                p += s[i];
            }
            else{
                result.push_back(p);
                p ="";
            }
        }
        return result;
    }
};