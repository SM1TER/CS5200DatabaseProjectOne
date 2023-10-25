import sqlite3
import os

class Relation:
    # x -> y
    def __init__(self, xToY):
        self.x: str = xToY[0]
        self.y: str = xToY[1]

def findPrimaryKeys(relations: list[Relation]):
    k = []
    for r in relations:
        k.append(r.x)
    means = []
    for r in relations:
        means.append(r.y)
    for m in means:
        if(m in k):
            k.remove(m)
    return list(set(k))

def constructCreateTableQuery(tableName, keys, primaryKeys):
    query = f'CREATE TABLE IF NOT EXISTS {tableName}('
    for x in keys:
        query = f'{query}{x} TEXT'
        if(x in primaryKeys):
            query = f'{query} KEY'
        if(keys[-1] != x):
            query = f'{query},'

    query = f'{query})'
    return query
try:
    os.remove('school.db') # removes old school.db file
except: 
    print('file not found')
connection = sqlite3.connect('school.db') # create a new students database file
cursor = connection.cursor() # creates a cursor to interact with the database

# creates a table called students
cursor.execute("""
CREATE TABLE IF NOT EXISTS
students(
    studentId TEXT,
    firstName TEXT,
    lastName TEXT,
    course TEXT,
    professor TEXT,
    professorEmail TEXT,
    courseStart TEXT,
    courseEnd TEXT
)
""")

# parses the file and adds the rows
file = open('data/exampleInputTable1.csv', 'r')
file.readline()
for x in file:
    studentId, firstName, lastName, course, professor, professorEmail, courseStart, courseEnd = x.strip('\n').split(",")
    query = f'INSERT INTO students VALUES (\'{studentId}\', \'{firstName}\', \'{lastName}\', \'{course}\', \'{professor}\', \'{professorEmail}\', \'{courseStart}\', \'{courseEnd}\')'
    print(query)
    cursor.execute(query)
file.close()

# sanity check to see the data was added to the students table
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# commits the changes to the actual file. While they aren't commit it is a temporary change
connection.commit()

file = open('data/relations.txt', 'r')
relations = []
for x in file:
    relations.append(Relation(x.strip('\n').split('->')))

print('')
print(f'Primary keys {findPrimaryKeys(relations)}')

file = open('data/exampleInputTable1.csv', 'r')
k = file.readline().strip('\n').split(',')
cursor.execute(constructCreateTableQuery('testTable', k, findPrimaryKeys(relations)))

cursor.execute("SELECT * FROM testTable")
print(cursor.fetchall())
#input("Which normal form level would you like?")