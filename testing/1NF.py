import sqlite3
import os
from ..src import helper

files = []
fileNames = [1]
for fileName in fileNames:
    file = open(f'{fileName}.csv','r')
    files = file.read()
    file.close()

connection = sqlite3.connect('1nf.db')
cursor = connection.cursor()
for tableName in fileNames:
    helper.createTable(tableName, cursor, k=files[tableName-1][0].strip('\n').split(','))
