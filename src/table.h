#ifndef table_h
#define table_h

#include <sstream>;
#include <vector>;
#include <string>;
#include <functional>;
#include "row.h";

using namespace std;

class Table {
    public:
        Table() {}
        Table(string columns) {
            stringstream ss(columns);
            while (ss.good()) {
                string substr;
                getline(ss, substr, ',');
                m_column_names.push_back(substr);
            }
        }
        Table(vector<string> columns) {
            for(auto & column: columns) {
                m_column_names.push_back(column);
            }
        }
        vector<string> get_column_names();
        void insert_into(Row row);
        Table select(string columns);
        Table where(string condition);
        Table mergeTables(Table table2);
    private:
        vector<Row> m_rows;
        vector<string> m_column_names;

};

#endif