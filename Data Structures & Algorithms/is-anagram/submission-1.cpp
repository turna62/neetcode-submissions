class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.size()!= t.size()){
            return false;
        }
        unordered_multiset<char> s1(s.begin(), s.end());
        unordered_multiset<char> s2(t.begin(), t.end());

        return s1 == s2;
    }
};
