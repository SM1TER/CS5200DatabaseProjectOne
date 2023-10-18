#include "table.h";


void Table::insert_into(Row row) {
    m_rows.push_back(row);
}

vector<string> Table::get_column_names() {
    return m_column_names;
}


// Select columnName1,columnName2,..., or use star
Table Table::select(string columns) {
    Table table;

    // copy of table
    if (columns == "*") {
        table = Table(m_column_names);
        for(int i = 0; i < m_rows.size(); i++) {
            table.insert_into(Row(m_rows[i]));
        }
        return table;
    }

    // subtable
    table = Table(columns);
    vector<string> o_columns = table.get_column_names();
    vector<pair<int, int>> connections;
    for(int i = 0; i < o_columns.size(); i++) {
        for(int j = 0; j < m_column_names.size(); j++) {
            if(o_columns[i] == m_column_names[j]) {
                pair<int, int> foundPair = pair(j, i);
                connections.push_back(foundPair);
                j = m_column_names.size();
            }
        }
    }

    for(int i = 0; i < m_rows.size(); i++) {
        Row newRow;
        for(int j = 0; j < connections.size(); j++) {
            newRow.data.push_back(m_rows[i].data[connections[j].first]);
        }
        table.insert_into(newRow);
    }
    return table;
}

/*sample commands no spaces
    columnName1=value
    columnName1<value, only usable for pure numbers
    columnName1=value&&columnName2=value2
    columnName1=value||columnName2=value2
*/
Table Table::where(string condition) {
    Table table = Table(m_column_names);

    return table;
}

Table Table::mergeTables(Table table2) {
    // find common property
}