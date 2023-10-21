class Row:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        rowString = ""
        for key, value in self.data.items():
            rowString = rowString + "  "+ value.ljust(len(key)+2," ")
        rowString = rowString + "\n"
        return rowString
        
class Table:
    def __init__(self, columnNames, rows) -> None:
        self.columnNames = columnNames
        self.rows = rows
    def __str__(self) -> str:
        tableString = ""
        for x in self.columnNames:
            tableString = tableString + "  "+ f'{x}'.ljust(len(x)+2)
        tableString = tableString + "\n"
        for x in range(len(self.rows)):
            tableString = tableString + str(self.rows[x])
        return tableString

def parseCSVFile(filePath):
    file = open(f'{filePath}.csv', "r")
    columnNames = file.readline().split(",")
    rows = []
    for x in file:
        rowList = x.split(",")
        row = {}
        for y in range(len(rowList)):
            row[columnNames[y]] = rowList[y]
        rows.append(Row(row))
    table = Table(columnNames, rows)
    file.close()
    return table

tables = parseCSVFile("data/exampleInputTable1")
print(tables)