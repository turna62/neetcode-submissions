class Solution {
public:

    string encode(vector<string>& strs) {

        string enc = "";

        for(int i=0; i< strs.size(); i++){
            enc+=(strs[i]);
            enc+=("]");
        }

        return enc;
    }

    vector<string> decode(string s) {

        vector<string> result;
        string st = "";

        for(int i=0; i< s.size(); i++){
        
            if(s[i]==']'){
                result.push_back(st);
                st = "";
                continue;
            }

            st+=(s[i]);

        }

        return result;
    }
};
