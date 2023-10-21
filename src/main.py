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

os.remove('school.db') # removes old school.db file 
connection = sqlite3.connect('school.db') # create a new students database file
cursor = connection.cursor() # creates a cursor to interact with the database

# creates a table called students
cursor.execute("""
CREATE TABLE IF NOT EXISTS
students(
    studentId INTEGER,
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
    query = f'INSERT INTO students VALUES ({studentId}, \'{firstName}\', \'{lastName}\', \'{course}\', \'{professor}\', \'{professorEmail}\', \'{courseStart}\', \'{courseEnd}\')'
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

print(f'Primary keys {findPrimaryKeys(relations)}')
#input("Which normal form level would you like?")