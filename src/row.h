#ifndef row_h
#define row_h

#include <vector>;
#include <string>;

using namespace std;

class Row {
    public:
        Row() {}
        Row(const Row& row) {
            for(int i = 0; i < row.data.size(); i++) {
                data.push_back(row.data[i]);
            }
        }
        vector<string> data;

};

#endif