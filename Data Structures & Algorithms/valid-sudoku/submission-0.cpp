class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> track;
        
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if(board[i][j] != '.'){
                    string rows = "row" + to_string(i) + board[i][j];
                    string cols = "col" + to_string(j) + board[i][j];
                    string sub_box = "sub_box" + to_string(i/3) + to_string(j/3) + board[i][j];

                    if(track.count(rows) or track.count(cols) or track.count(sub_box)){
                        return false;
                    }

                    track.insert(rows);
                    track.insert(cols);
                    track.insert(sub_box);
                }
            }
        }
        return true;
    }
};